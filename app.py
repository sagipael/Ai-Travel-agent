from flask import Flask, render_template, request, jsonify
import os
import json
import threading
import time
from datetime import datetime, timedelta
import google.generativeai as genai
import requests
from apscheduler.schedulers.background import BackgroundScheduler
import sqlite3

app = Flask(__name__)

# Configuration from environment variables
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')
DB_PATH = os.environ.get('DB_PATH', 'travel_agent.db')

# Initialize Gemini AI
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-2.0-flash-exp')

# Initialize scheduler
scheduler = BackgroundScheduler()
scheduler.start()

# Database setup
def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS searches
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  destinations TEXT,
                  source_country TEXT,
                  date_start TEXT,
                  date_end TEXT,
                  check_interval INTEGER,
                  allow_non_direct INTEGER DEFAULT 0,
                  custom_filter TEXT,
                  created_at TEXT,
                  active INTEGER DEFAULT 1)''')
    c.execute('''CREATE TABLE IF NOT EXISTS results
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  search_id INTEGER,
                  destination TEXT,
                  date TEXT,
                  price REAL,
                  details TEXT,
                  checked_at TEXT,
                  FOREIGN KEY (search_id) REFERENCES searches(id))''')
    conn.commit()
    conn.close()

init_db()

def row_to_search_dict(row):
    """Helper function to convert database row to search dictionary"""
    return {
        "id": row["id"],
        "destinations": json.loads(row["destinations"]),
        "source_country": row["source_country"] if row["source_country"] else "Not specified",
        "date_start": row["date_start"],
        "date_end": row["date_end"],
        "check_interval": row["check_interval"],
        "allow_non_direct": bool(row["allow_non_direct"]) if "allow_non_direct" in row.keys() else False,
        "custom_filter": row["custom_filter"] if "custom_filter" in row.keys() else "",
        "created_at": row["created_at"]
    }

def send_telegram_message(message):
    """Send message to Telegram"""
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram credentials not configured")
        return False
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=data)
        return response.status_code == 200
    except Exception as e:
        print(f"Error sending Telegram message: {e}")
        return False

def search_flights_with_ai(source_country, destination, date_start, date_end, allow_non_direct=False, custom_filter=""):
    """Use Gemini AI to search for flight information"""
    if not GEMINI_API_KEY:
        return {"error": "Gemini API key not configured"}
    
    flight_type = "direct and connecting flights" if allow_non_direct else "direct flights only"
    custom_filter_text = f"\n\nAdditional filter: {custom_filter}" if custom_filter else ""
    
    prompt = f"""You are a travel agent AI assistant. Search for flight options from {source_country} to {destination} 
    between {date_start} and {date_end}. Focus on {flight_type}.{custom_filter_text}
    
    Provide realistic flight options with:
    1. 3-5 different flight options with specific airlines/providers
    2. Price estimates for each option (economy class)
    3. Flight types (direct/connecting)
    4. Booking links (use realistic booking sites like Skyscanner, Kayak, Google Flights, Momondo, or airline websites)
    5. Best times to book
    6. Any seasonal factors affecting prices
    
    Format your response as JSON with the following structure:
    {{
        "source": "{source_country}",
        "destination": "{destination}",
        "date_range": "{date_start} to {date_end}",
        "flight_options": [
            {{
                "provider": "Airline name or booking site",
                "price": 450,
                "flight_type": "Direct" or "1 stop" or "2+ stops",
                "booking_link": "https://www.example.com/book?...",
                "details": "Brief description"
            }}
        ],
        "estimated_price_range": {{"min": 0, "max": 0}},
        "best_booking_time": "",
        "tips": []
    }}
    """
    
    try:
        response = model.generate_content(prompt)
        result_text = response.text
        
        # Try to extract JSON from the response
        if "```json" in result_text:
            json_start = result_text.find("```json") + 7
            json_end = result_text.find("```", json_start)
            result_text = result_text[json_start:json_end].strip()
        elif "```" in result_text:
            json_start = result_text.find("```") + 3
            json_end = result_text.find("```", json_start)
            result_text = result_text[json_start:json_end].strip()
        
        result = json.loads(result_text)
        return result
    except Exception as e:
        print(f"Error with AI search: {e}")
        # Return simulated data as fallback
        return {
            "source": source_country,
            "destination": destination,
            "date_range": f"{date_start} to {date_end}",
            "flight_options": [
                {
                    "provider": "Skyscanner",
                    "price": 450,
                    "flight_type": "Direct",
                    "booking_link": f"https://www.skyscanner.com/transport/flights/{source_country.lower()}/{destination.lower()}/",
                    "details": "Morning departure, good price"
                },
                {
                    "provider": "Google Flights",
                    "price": 380,
                    "flight_type": "1 stop",
                    "booking_link": "https://www.google.com/flights",
                    "details": "Afternoon departure via hub"
                },
                {
                    "provider": "Kayak",
                    "price": 520,
                    "flight_type": "Direct",
                    "booking_link": "https://www.kayak.com/flights",
                    "details": "Evening departure, premium time"
                }
            ],
            "estimated_price_range": {"min": 300, "max": 800},
            "best_booking_time": "2-3 months in advance",
            "tips": ["Book on Tuesday or Wednesday for better prices", "Use incognito mode when searching"]
        }

def check_flights(search_id, source_country, destinations, date_start, date_end, allow_non_direct=False, custom_filter=""):
    """Check flights for a specific search"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    results_message = f"🛫 *Flight Update for {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n"
    results_message += f"✈️ *From:* {source_country}\n\n"
    
    for destination in destinations:
        result = search_flights_with_ai(source_country, destination, date_start, date_end, allow_non_direct, custom_filter)
        
        # Store result in database
        c.execute('''INSERT INTO results (search_id, destination, date, price, details, checked_at)
                     VALUES (?, ?, ?, ?, ?, ?)''',
                  (search_id, destination, date_start, 
                   result.get('estimated_price_range', {}).get('min', 0),
                   json.dumps(result), datetime.now().isoformat()))
        
        # Format message
        results_message += f"📍 *{destination}*\n"
        price_range = result.get('estimated_price_range', {})
        results_message += f"💰 Price range: ${price_range.get('min', 'N/A')} - ${price_range.get('max', 'N/A')}\n"
        results_message += f"📅 Best booking: {result.get('best_booking_time', 'N/A')}\n\n"
    
    conn.commit()
    conn.close()
    
    # Send to Telegram
    send_telegram_message(results_message)
    
    return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def create_search():
    """Create a new flight search"""
    data = request.json
    destinations = data.get('destinations', [])
    source_country = data.get('source_country', '')
    date_start = data.get('date_start')
    date_end = data.get('date_end')
    check_interval = data.get('check_interval', 24)  # hours
    allow_non_direct = 1 if data.get('allow_non_direct', False) else 0
    custom_filter = data.get('custom_filter', '')
    
    if not destinations or not date_start or not date_end or not source_country:
        return jsonify({"error": "Missing required fields"}), 400
    
    # Save to database
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''INSERT INTO searches (destinations, source_country, date_start, date_end, check_interval, allow_non_direct, custom_filter, created_at)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
              (json.dumps(destinations), source_country, date_start, date_end, check_interval, allow_non_direct, custom_filter, datetime.now().isoformat()))
    search_id = c.lastrowid
    conn.commit()
    conn.close()
    
    # Do initial check
    check_flights(search_id, source_country, destinations, date_start, date_end, bool(allow_non_direct), custom_filter)
    
    # Schedule periodic checks
    scheduler.add_job(
        func=check_flights,
        trigger='interval',
        hours=check_interval,
        args=[search_id, source_country, destinations, date_start, date_end, bool(allow_non_direct), custom_filter],
        id=f'search_{search_id}',
        replace_existing=True
    )
    
    return jsonify({
        "success": True,
        "search_id": search_id,
        "message": "Flight search created and scheduled"
    })

@app.route('/api/results')
def get_results():
    """Get all flight search results"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''SELECT r.*, s.destinations 
                 FROM results r 
                 JOIN searches s ON r.search_id = s.id 
                 ORDER BY r.checked_at DESC 
                 LIMIT 100''')
    rows = c.fetchall()
    conn.close()
    
    results = []
    for row in rows:
        results.append({
            "id": row[0],
            "search_id": row[1],
            "destination": row[2],
            "date": row[3],
            "price": row[4],
            "details": json.loads(row[5]) if row[5] else {},
            "checked_at": row[6]
        })
    
    return jsonify(results)

@app.route('/api/searches')
def get_searches():
    """Get all active searches"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM searches WHERE active = 1 ORDER BY created_at DESC')
    rows = c.fetchall()
    conn.close()
    
    searches = [row_to_search_dict(row) for row in rows]
    return jsonify(searches)

@app.route('/api/search/<int:search_id>', methods=['DELETE'])
def delete_search(search_id):
    """Delete/deactivate a search"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('UPDATE searches SET active = 0 WHERE id = ?', (search_id,))
    conn.commit()
    conn.close()
    
    # Remove scheduled job
    try:
        scheduler.remove_job(f'search_{search_id}')
    except Exception:
        pass  # Job may not exist
    
    return jsonify({"success": True})

@app.route('/api/search/<int:search_id>', methods=['GET'])
def get_search(search_id):
    """Get a specific search by ID"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM searches WHERE id = ?', (search_id,))
    row = c.fetchone()
    conn.close()
    
    if not row:
        return jsonify({"error": "Search not found"}), 404
    
    search = row_to_search_dict(row)
    return jsonify(search)

@app.route('/api/search/<int:search_id>', methods=['PUT'])
def update_search(search_id):
    """Update an existing search"""
    data = request.json
    destinations = data.get('destinations', [])
    source_country = data.get('source_country', '')
    date_start = data.get('date_start')
    date_end = data.get('date_end')
    check_interval = data.get('check_interval', 24)
    allow_non_direct = 1 if data.get('allow_non_direct', False) else 0
    custom_filter = data.get('custom_filter', '')
    
    if not destinations or not date_start or not date_end or not source_country:
        return jsonify({"error": "Missing required fields"}), 400
    
    # Update database
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''UPDATE searches 
                 SET destinations = ?, source_country = ?, date_start = ?, date_end = ?, 
                     check_interval = ?, allow_non_direct = ?, custom_filter = ?
                 WHERE id = ?''',
              (json.dumps(destinations), source_country, date_start, date_end, 
               check_interval, allow_non_direct, custom_filter, search_id))
    conn.commit()
    conn.close()
    
    # Remove old scheduled job
    try:
        scheduler.remove_job(f'search_{search_id}')
    except Exception:
        pass  # Job may not exist
    
    # Schedule new periodic checks with updated parameters
    scheduler.add_job(
        func=check_flights,
        trigger='interval',
        hours=check_interval,
        args=[search_id, source_country, destinations, date_start, date_end, bool(allow_non_direct), custom_filter],
        id=f'search_{search_id}',
        replace_existing=True
    )
    
    return jsonify({
        "success": True,
        "message": "Search updated successfully"
    })

@app.route('/api/chart/<destination>')
def get_chart_data(destination):
    """Get price history for chart"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''SELECT date, price, checked_at 
                 FROM results 
                 WHERE destination = ? 
                 ORDER BY checked_at ASC''', (destination,))
    rows = c.fetchall()
    conn.close()
    
    data = {
        "labels": [row[2] for row in rows],
        "prices": [row[1] for row in rows]
    }
    
    return jsonify(data)

if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    port = int(os.environ.get('PORT', 5008))
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
