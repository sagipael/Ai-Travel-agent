# How to Use My AI Travel Agent

This guide provides step-by-step instructions for using My AI Travel Agent as an end user. Follow these simple steps to start tracking flight prices and finding the best deals.

## Quick Start (5 Minutes)

### Step 1: Access the Application
1. Open your web browser
2. Navigate to: `http://localhost:5000` (or your configured URL)
3. You should see the My AI Travel Agent dashboard

### Step 2: Add Your First Destination
1. Locate the **"Destination"** input field at the top of the page
2. Type the name of your destination city (e.g., "Paris", "Tokyo", "New York")
   - You can also use airport codes (e.g., "CDG", "NRT", "JFK")
3. Click the **"Add Destination"** button
4. Your destination will appear in the list below

**Example**: Type "London" and click "Add Destination"

### Step 3: Select Travel Dates
1. Find the **"Departure Date"** field
2. Click on the calendar icon
3. Select your desired departure date
4. (Optional) Select a return date if you're booking a round trip
5. Click **"Add Date Range"** button

**Example**: Select March 15, 2026 for departure and March 22, 2026 for return

### Step 4: Start Monitoring
1. Find the **"Check Interval"** dropdown menu
2. Select how often you want to check prices:
   - **Every hour** - For urgent travel or last-minute deals
   - **Every 6 hours** - Recommended for most users
   - **Every 12 hours** - For advance planning
   - **Daily** - For long-term monitoring
3. Click the **"Start Monitoring"** button
4. The status indicator will change to "Active"

**Recommendation**: Start with "Every 6 hours" for a good balance

### Step 5: View Results
1. Scroll down to the **Results** section
2. Wait for the first check to complete (may take 1-2 minutes)
3. View the price graph and current best price
4. Check back regularly or wait for Telegram notifications

## Detailed Instructions

## Setting Up Telegram Notifications

To receive instant price alerts on your phone:

### Step 1: Create a Telegram Bot
1. Open Telegram app on your phone
2. Search for "@BotFather"
3. Send the command: `/newbot`
4. Follow the prompts to create your bot:
   - Choose a name for your bot (e.g., "My Travel Agent")
   - Choose a username (must end in "bot", e.g., "mytravelagent_bot")
5. BotFather will give you a **bot token** - save this!
   - Example: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`

### Step 2: Get Your Chat ID
1. Start a chat with your new bot (click the link BotFather provides)
2. Send any message to your bot (e.g., "Hello")
3. Visit this URL in your browser: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
   - Replace `<YOUR_BOT_TOKEN>` with your actual bot token
4. Look for the "chat" section and find the "id" number
   - Example: `"id": 123456789`
5. Save this Chat ID

### Step 3: Configure Environment Variables
1. If running with Docker, set these environment variables:
   ```
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   TELEGRAM_CHAT_ID=your_chat_id_here
   ```
2. The application will automatically start sending notifications

### Step 4: Test Notifications
1. After configuration, start monitoring a flight
2. You should receive a confirmation message in Telegram
3. Subsequent notifications will arrive when prices change

## Using the Price Graphs

Understanding the visual data:

### Reading the Graph
- **Horizontal axis (X)**: Shows time (dates and times of price checks)
- **Vertical axis (Y)**: Shows price in your currency
- **Blue line**: The actual price trend over time
- **Dots on the line**: Individual price checks

### Interactive Features
1. **Hover over points**: See exact price and timestamp
2. **Zoom**: Click and drag to zoom into a time period
3. **Reset view**: Double-click to reset to full view
4. **Compare**: Switch between destination tabs to compare

### Identifying Good Deals
Look for these patterns:
- **Downward trends**: Prices are dropping, might drop more
- **Sudden drops**: Good time to book
- **Flat lines**: Prices are stable
- **Upward trends**: Prices increasing, consider booking soon

## Managing Multiple Destinations

You can track several destinations at once:

### Adding Multiple Destinations
1. Add your first destination (as described above)
2. Enter another destination in the input field
3. Click "Add Destination" again
4. Repeat for all destinations you want to track

**Example Trip Planning**:
- Add "Paris, France"
- Add "Rome, Italy"
- Add "Barcelona, Spain"
- Compare prices to decide where to go!

### Viewing Different Destinations
1. Scroll to the Results section
2. You'll see tabs for each destination
3. Click on a tab to view that destination's data
4. Each has its own price graph and best price

### Removing Destinations
1. Find the destination in your list
2. Click the **"Remove"** or **"X"** button next to it
3. Confirm if prompted
4. The destination will stop being monitored

## Setting Date Ranges

### Single Date Range
For a specific trip:
1. Select departure date: March 15, 2026
2. Select return date: March 22, 2026
3. Click "Add Date Range"

### Multiple Date Ranges (Flexible Travel)
If you're flexible:
1. Add first range: March 15-22, 2026
2. Click "Add Date Range"
3. Add second range: March 22-29, 2026
4. Click "Add Date Range"
5. System will find best prices across all ranges

### One-Way Trips
1. Select departure date only
2. Leave return date empty
3. Click "Add Date Range"

## Understanding Price Alerts

You'll receive Telegram alerts for:

### 1. Significant Price Drops
When a price drops by more than 10%:
```
🛫 Price Drop Alert!
Paris (CDG): $450 → $405
You save: $45 (10%)
```

### 2. Best Deal Found
When AI identifies an exceptional price:
```
⭐ Best Deal Found!
Tokyo (NRT): $680
This is 25% below average!
Book now: [Link]
```

### 3. Price Increase Warnings
If you're tracking a flight and price goes up:
```
⚠️ Price Increase
London (LHR): $320 → $385
Consider booking soon if this is your target destination
```

### 4. Daily Summary (Optional)
End of day overview:
```
📊 Daily Summary
Paris: $450 (↓ $20)
London: $385 (↑ $15)
Tokyo: $680 (→ no change)
```

## Best Practices for Users

### When to Book
Based on AI analysis and price trends:

1. **2-3 Months Before**: Usually optimal
2. **6-8 Weeks Before**: Often see best prices
3. **Last Minute**: Sometimes good deals, but risky
4. **Avoid Peak Times**: Holidays, weekends often more expensive

### How to Save Money
1. **Be Flexible**: 
   - Try different date ranges
   - Consider nearby airports
   - Weekday travel often cheaper

2. **Monitor Early**:
   - Start tracking 3-4 months before travel
   - Watch price patterns
   - Book when you see a significant drop

3. **Use Multiple Destinations**:
   - Compare similar destinations
   - Sometimes nearby cities are much cheaper
   - Example: Flying to Oakland vs. San Francisco

4. **Check the Graph**:
   - Look for price patterns
   - Book during dips
   - Avoid booking during peaks

### Optimizing Your Experience
1. **Check Interval**:
   - Urgent travel: Every hour
   - Normal planning: Every 6 hours
   - Long-term planning: Daily

2. **Number of Destinations**:
   - Start with 2-3 destinations
   - Add more as needed
   - Too many can slow down checks

3. **Date Ranges**:
   - Add 2-3 flexible ranges
   - More ranges = better deal finding
   - But more checks = slower system

## Common User Scenarios

### Scenario 1: Planning a Vacation
**Goal**: Find the cheapest time to visit Europe

**Steps**:
1. Add multiple European cities (Paris, Rome, Barcelona)
2. Add wide date ranges (entire month)
3. Set check interval to "Every 12 hours"
4. Monitor for 2-3 weeks
5. Book when you see the best deal

### Scenario 2: Booking a Specific Trip
**Goal**: Get best price for specific dates

**Steps**:
1. Add your destination
2. Add your exact travel dates
3. Set check interval to "Every 6 hours"
4. Enable Telegram notifications
5. Book when price drops significantly

### Scenario 3: Flexible Traveler
**Goal**: Go anywhere that's cheap

**Steps**:
1. Add 5-10 destinations you'd like to visit
2. Add flexible date ranges
3. Set daily check interval
4. Wait for AI to find best deals
5. Book the cheapest destination!

### Scenario 4: Last-Minute Travel
**Goal**: Find deals for travel this week

**Steps**:
1. Add destinations
2. Add date ranges starting today
3. Set "Every hour" check interval
4. Turn on all notifications
5. Be ready to book immediately

## Frequently Asked Questions (FAQs)

### Q: How long should I monitor before booking?
**A**: Ideally, start monitoring 2-3 months before your trip. Most users find the best deals 6-8 weeks before departure.

### Q: Can I monitor international and domestic flights?
**A**: Yes! The system works for both. Just enter any destination city or airport code.

### Q: How accurate are the prices?
**A**: Prices are checked in real-time from multiple sources. However, final prices may vary slightly when booking due to taxes, fees, and availability.

### Q: What if I see a great price?
**A**: Act quickly! Flight prices can change rapidly. The system shows current prices, but they can increase within hours.

### Q: Can I save my searches?
**A**: Yes, your destinations and date ranges are saved automatically. You can stop and resume monitoring anytime.

### Q: How many destinations can I track?
**A**: You can track multiple destinations, but for best performance, we recommend 3-5 active destinations at a time.

### Q: Do I need to keep the browser open?
**A**: No! Once monitoring is started, it runs in the background. You'll receive Telegram notifications even if your browser is closed.

### Q: What if I miss a deal?
**A**: Don't worry! The system continuously monitors and will alert you to the next good deal. Enable Telegram notifications to never miss out.

### Q: Can multiple users share one instance?
**A**: The application is designed for single-user use. Each user should have their own instance for best results.

### Q: Are there any costs to use this?
**A**: The application itself is free, but you'll need to pay for flights when you book them through the airlines or booking sites.

## Tips for Maximum Savings

### 💡 Pro Tips

1. **Compare Multiple Airports**
   - Example: NYC has JFK, LGA, and EWR
   - Sometimes significant price differences
   - Add all as separate destinations

2. **Use Date Flexibility**
   - Flying Tuesday/Wednesday often cheaper
   - Avoid Friday/Sunday for best prices
   - Add multiple date options

3. **Set Target Prices**
   - Research average prices first
   - Set expectations for your budget
   - Book when you meet your target

4. **Monitor Seasonality**
   - Use price graphs to see patterns
   - Low season = lower prices
   - Avoid holidays and peak times

5. **Act on Good Deals**
   - Great deals don't last long
   - Have payment info ready
   - Book within hours of alert

6. **Cross-Reference**
   - Verify prices on airline sites
   - Check multiple booking platforms
   - Look for additional fees

## Getting Help

### If You Need Assistance

1. **Check This Guide**: Most questions are answered here
2. **Review User Guide**: See USER_GUIDE.md for detailed information
3. **View Screenshots**: Check SCREENSHOTS.md for visual references
4. **Check Logs**: Look at application logs for error messages
5. **GitHub Issues**: Report bugs or request features on GitHub

### Contact Information
- GitHub Repository: [Link to repo]
- Documentation: See README.md
- Issues: Submit through GitHub Issues

## Next Steps

Now that you know how to use My AI Travel Agent:

1. ✅ Start adding your destinations
2. ✅ Set up Telegram notifications
3. ✅ Configure your monitoring preferences
4. ✅ Begin tracking prices
5. ✅ Book your dream trip at the best price!

Happy travels! ✈️🌍

---

*Last Updated: February 2026*
