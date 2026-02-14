from flask import Flask, render_template, request, jsonify
import os
import json
import threading
import time
from datetime import datetime, timedelta
import google.generativeai as genai
import requests
from apscheduler.schedules import IntervalScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import sqlite3

app = Flask(__name__)

# Configuration from environment variables
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

# Initialize Gemini AI
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-2.0-flash-exp')

# Initialize scheduler
scheduler = BackgroundScheduler()
scheduler.start()

# Database setup
def init_db():
    conn = sqlite3.connect('travel_agent.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS searches
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  destinations TEXT,
                  date_start TEXT,
                  date_end TEXT,
                  check_interval INTEGER,
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

def search_flights_with_ai(destination, date_start, date_end):
    """Use Gemini AI to search for flight information"""
    if not GEMINI_API_KEY:
        return {"error": "Gemini API key not configured"}
    
    prompt = f"""You are a travel agent AI assistant. Search for flight options to {destination} 
    between {date_start} and {date_end}. 
    
    Provide a realistic estimate of:
    1. Typical flight prices (economy class)
    2. Best times to book
    3. Price range expectations
    4. Any seasonal factors affecting prices
    
    Format your response as JSON with the following structure:
    {{
        "destination": "{destination}",
        "date_range": "{date_start} to {date_end}",
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
            "destination": destination,
            "date_range": f"{date_start} to {date_end}",
            "estimated_price_range": {"min": 300, "max": 800},
            "best_booking_time": "2-3 months in advance",
            "tips": ["Book on Tuesday or Wednesday for better prices", "Use incognito mode when searching"]
        }

def check_flights(search_id, destinations, date_start, date_end):
    """Check flights for a specific search"""
    conn = sqlite3.connect('travel_agent.db')
    c = conn.cursor()
    
    results_message = f"🛫 *Flight Update for {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n"
    
    for destination in destinations:
        result = search_flights_with_ai(destination, date_start, date_end)
        
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
    date_start = data.get('date_start')
    date_end = data.get('date_end')
    check_interval = data.get('check_interval', 24)  # hours
    
    if not destinations or not date_start or not date_end:
        return jsonify({"error": "Missing required fields"}), 400
    
    # Save to database
    conn = sqlite3.connect('travel_agent.db')
    c = conn.cursor()
    c.execute('''INSERT INTO searches (destinations, date_start, date_end, check_interval, created_at)
                 VALUES (?, ?, ?, ?, ?)''',
              (json.dumps(destinations), date_start, date_end, check_interval, datetime.now().isoformat()))
    search_id = c.lastrowid
    conn.commit()
    conn.close()
    
    # Do initial check
    check_flights(search_id, destinations, date_start, date_end)
    
    # Schedule periodic checks
    scheduler.add_job(
        func=check_flights,
        trigger='interval',
        hours=check_interval,
        args=[search_id, destinations, date_start, date_end],
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
    conn = sqlite3.connect('travel_agent.db')
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
    conn = sqlite3.connect('travel_agent.db')
    c = conn.cursor()
    c.execute('SELECT * FROM searches WHERE active = 1 ORDER BY created_at DESC')
    rows = c.fetchall()
    conn.close()
    
    searches = []
    for row in rows:
        searches.append({
            "id": row[0],
            "destinations": json.loads(row[1]),
            "date_start": row[2],
            "date_end": row[3],
            "check_interval": row[4],
            "created_at": row[5]
        })
    
    return jsonify(searches)

@app.route('/api/search/<int:search_id>', methods=['DELETE'])
def delete_search(search_id):
    """Delete/deactivate a search"""
    conn = sqlite3.connect('travel_agent.db')
    c = conn.cursor()
    c.execute('UPDATE searches SET active = 0 WHERE id = ?', (search_id,))
    conn.commit()
    conn.close()
    
    # Remove scheduled job
    try:
        scheduler.remove_job(f'search_{search_id}')
    except:
        pass
    
    return jsonify({"success": True})

@app.route('/api/chart/<destination>')
def get_chart_data(destination):
    """Get price history for chart"""
    conn = sqlite3.connect('travel_agent.db')
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
    app.run(host='0.0.0.0', port=5000, debug=True)
