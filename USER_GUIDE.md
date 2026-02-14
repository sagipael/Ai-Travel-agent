# My AI Travel Agent - User Guide

Welcome to My AI Travel Agent! This guide will help you get the most out of your AI-powered flight price tracker.

## Table of Contents
1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Main Features](#main-features)
4. [Using the Web Interface](#using-the-web-interface)
5. [Understanding Results](#understanding-results)
6. [Telegram Notifications](#telegram-notifications)
7. [Best Practices](#best-practices)
8. [Troubleshooting](#troubleshooting)

## Introduction

My AI Travel Agent is an intelligent flight price monitoring tool that helps you find the best deals for your travel plans. Using advanced AI technology (Gemini 2.5 Flash), it continuously monitors flight prices and alerts you when it finds great deals.

### What Can It Do?
- 🔍 **Smart Search**: Monitor multiple destinations and date ranges simultaneously
- 📊 **Price Tracking**: Track price trends over time with interactive graphs
- 🔔 **Instant Alerts**: Get notified via Telegram when prices drop
- 📈 **Visual Analytics**: See price trends and compare destinations
- ⏰ **Automated Monitoring**: Set custom check intervals

## Getting Started

### Prerequisites
Before using My AI Travel Agent, you'll need:
- A Telegram account and bot setup (for notifications)
- Internet connection
- Web browser (Chrome, Firefox, Safari, or Edge)

### First Time Setup
1. Access the web interface at `http://localhost:5000` (or your configured URL)
2. You'll see the main dashboard with configuration options
3. No login required - start using immediately!

## Main Features

### 1. Destination Management
Add multiple destinations you're interested in traveling to:
- Enter destination city or airport code
- Add as many destinations as needed
- Edit or remove destinations anytime

### 2. Date Range Selection
Configure flexible date ranges:
- Select start and end dates for your travel window
- Add multiple date ranges for each destination
- Ideal for flexible travelers

### 3. Price Monitoring
Set your monitoring preferences:
- Choose check intervals (hourly, daily, etc.)
- View real-time price updates
- Track historical price data

### 4. Results Dashboard
View comprehensive results:
- Interactive price graphs for each destination
- Best available prices highlighted
- Price trend indicators
- Historical data comparison

## Using the Web Interface

### Dashboard Overview
The main dashboard consists of several sections:

#### 1. **Destination Configuration Panel** (Top Section)
- Input field for destination cities/airports
- "Add Destination" button
- List of current destinations with remove options

#### 2. **Date Range Selector** (Middle Section)
- Departure date picker
- Return date picker (optional)
- "Add Date Range" button
- Display of configured date ranges

#### 3. **Monitoring Settings** (Right Panel)
- Check interval selector (dropdown)
  - Every hour
  - Every 6 hours
  - Every 12 hours
  - Daily
- "Start Monitoring" / "Stop Monitoring" toggle button
- Current status indicator

#### 4. **Results Display** (Bottom Section)
- Tabbed interface for each destination
- Price graphs showing trends over time
- Best price card highlighting the lowest fare
- Quick action buttons

### Adding Your First Flight Search

**Step 1: Add Destination**
1. Click on the "Destination" input field
2. Type the city name or airport code (e.g., "New York" or "JFK")
3. Click "Add Destination" button
4. Your destination appears in the list below

**Step 2: Set Date Range**
1. Click on the "Departure Date" calendar icon
2. Select your desired departure date
3. (Optional) Select return date if needed
4. Click "Add Date Range"
5. The date range is added to your search

**Step 3: Configure Monitoring**
1. Select check interval from dropdown (recommended: Every 6 hours)
2. Click "Start Monitoring" button
3. Status changes to "Active - Monitoring"

**Step 4: View Results**
1. Scroll down to the Results section
2. Click on destination tabs to switch between searches
3. View price graphs and best deals

### Understanding the Price Graph

The interactive price graph shows:
- **X-axis**: Timeline (dates/times of checks)
- **Y-axis**: Price in your local currency
- **Blue line**: Price trend over time
- **Green markers**: Price drops
- **Red markers**: Price increases
- **Hover**: See exact price and timestamp

### Managing Multiple Destinations

You can monitor multiple destinations simultaneously:
1. Add multiple destinations using the same process
2. Each destination gets its own tab in the results
3. Graphs show comparative data
4. Best prices highlighted for each destination

## Understanding Results

### Result Cards
Each result includes:
- **Destination**: Where you're flying to
- **Current Best Price**: Lowest available price right now
- **Price History**: Graph showing price changes
- **Last Updated**: When the price was last checked
- **Price Change**: Indicator showing if price went up/down

### Price Indicators
- 🟢 **Green**: Price decreased since last check
- 🔴 **Red**: Price increased since last check
- ⚪ **Gray**: Price unchanged
- ⭐ **Star**: Best price in the last 7 days

### Best Deal Notifications
When the AI finds an exceptional deal:
- Yellow highlight on the result card
- Automatic Telegram notification
- "Best Deal" badge displayed
- Recommended action message

## Telegram Notifications

### How It Works
My AI Travel Agent sends you real-time notifications via Telegram:

1. **Price Drop Alerts**: When prices decrease significantly
2. **Best Deal Found**: When AI identifies an exceptional price
3. **Daily Summary**: Overview of all monitored flights (optional)
4. **Status Updates**: When monitoring starts/stops

### Notification Format
Each notification includes:
```
🛫 Flight Deal Alert!

Destination: Paris (CDG)
Current Price: $450
Previous Price: $520
You Save: $70 (13.5%)

Date Range: Mar 15 - Mar 22
Last Checked: 2 minutes ago

View Details: [Link to Dashboard]
```

### Managing Notifications
Configure notification settings:
- Minimum price drop threshold
- Frequency of updates
- Daily summary preference
- Quiet hours (no notifications during certain times)

## Best Practices

### Getting the Best Results

1. **Be Flexible with Dates**
   - Add wider date ranges for better deals
   - Consider weekday vs. weekend travel
   - Avoid major holidays for lower prices

2. **Check Multiple Destinations**
   - Compare similar destinations
   - Consider alternative airports nearby
   - Look at regional hubs for connections

3. **Set Appropriate Intervals**
   - Hourly checks for urgent travel
   - Daily checks for planned trips
   - Balance between updates and system load

4. **Monitor Early**
   - Start monitoring 2-3 months before travel
   - Prices typically lowest 6-8 weeks before departure
   - Last-minute deals are rare but possible

5. **Use Price Graphs**
   - Identify price patterns and trends
   - Spot the best booking windows
   - Understand seasonal variations

### Optimization Tips

- **Multiple Date Ranges**: Add several date ranges to find the best deals
- **Regular Reviews**: Check your dashboard daily for new opportunities
- **Quick Actions**: Act fast when you see a great deal
- **Telegram Alerts**: Enable notifications to never miss a deal

## Troubleshooting

### Common Issues and Solutions

#### No Results Showing
**Problem**: Added destinations but no results appear
**Solutions**:
- Ensure monitoring is started (check status indicator)
- Wait for first check cycle to complete (based on your interval)
- Check internet connection
- Verify destination codes are valid

#### Telegram Not Receiving Notifications
**Problem**: Not getting Telegram alerts
**Solutions**:
- Verify bot token and chat ID are correctly configured
- Check if bot is started in Telegram (send /start command)
- Ensure notifications are enabled in settings
- Check your Telegram notification settings

#### Graph Not Displaying
**Problem**: Price graph is blank or not loading
**Solutions**:
- Refresh the page (F5)
- Clear browser cache
- Wait for more data points (at least 2 checks needed)
- Check browser console for errors

#### Prices Seem Outdated
**Problem**: Prices don't appear current
**Solutions**:
- Check "Last Updated" timestamp
- Verify monitoring is active
- Adjust check interval to more frequent
- Click manual refresh button if available

#### Application Not Responding
**Problem**: Interface is slow or unresponsive
**Solutions**:
- Reduce number of active destinations
- Increase check interval
- Clear browser cache and cookies
- Restart the Docker container

### Getting Help

If you continue experiencing issues:
1. Check the application logs for error messages
2. Verify all environment variables are set correctly
3. Ensure Docker container is running properly
4. Consult the technical documentation
5. Open an issue on GitHub with details

## Advanced Features

### Custom Filters
Set advanced search criteria:
- Maximum number of stops
- Preferred airlines
- Time of day preferences
- Maximum flight duration

### Export Data
Export your price tracking data:
- CSV format for Excel analysis
- PDF reports for record keeping
- Graph images for sharing

### Price Alerts
Configure custom alert rules:
- Target price threshold
- Percentage drop alerts
- Comparative alerts (vs. average)

## Privacy and Data

### What We Track
- Your search preferences (destinations, dates)
- Price history for your searches
- Your Telegram chat ID (for notifications)

### What We Don't Track
- Personal identification information
- Payment information
- Browsing history outside the app

### Data Storage
- All data stored locally in the container
- No data sold or shared with third parties
- Data automatically cleared after 90 days

## Tips for Budget Travelers

1. **Use Wide Date Ranges**: More flexibility = better deals
2. **Consider Nearby Airports**: Sometimes alternative airports are cheaper
3. **Monitor Multiple Destinations**: Compare costs across different options
4. **Book at the Right Time**: Usually 6-8 weeks before departure
5. **Set Price Alerts**: Let the AI notify you of the best deals
6. **Check Seasonal Trends**: Use the graph to identify low seasons

## Conclusion

My AI Travel Agent is designed to make finding affordable flights effortless. By leveraging AI technology and continuous monitoring, you can save time and money on your travel plans.

Happy travels! ✈️

---

**Need More Help?**
- Check the [How to Use Guide](HOW_TO_USE.md) for step-by-step instructions
- View [Screenshots](SCREENSHOTS.md) for visual reference
- Visit the GitHub repository for technical documentation
