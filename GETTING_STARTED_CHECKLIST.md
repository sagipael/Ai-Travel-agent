# Getting Started Checklist ✅

Use this checklist to get your My AI Travel Agent up and running quickly!

## Pre-Installation Checklist

Before you begin, make sure you have:

- [ ] Docker installed on your computer
  - Windows/Mac: Download [Docker Desktop](https://www.docker.com/products/docker-desktop)
  - Linux: Install Docker via your package manager
- [ ] A Google account (for Gemini API)
- [ ] A Telegram account
- [ ] Basic command-line knowledge (optional but helpful)

## Setup Checklist

### Step 1: Get API Credentials

#### Gemini API Token
- [ ] Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
- [ ] Sign in with your Google account
- [ ] Click "Get API Key" or "Create API Key"
- [ ] Copy your API token and save it somewhere safe
- [ ] Keep it secret - don't share it publicly!

#### Telegram Bot Setup
- [ ] Open Telegram on your phone or computer
- [ ] Search for `@BotFather`
- [ ] Send the command: `/newbot`
- [ ] Choose a name for your bot (e.g., "My Travel Agent")
- [ ] Choose a username ending in "bot" (e.g., "mytravelagent_bot")
- [ ] Copy the bot token that BotFather gives you
- [ ] Save this token safely

#### Get Your Telegram Chat ID
- [ ] Start a conversation with your new bot
- [ ] Send any message to your bot (e.g., "Hello")
- [ ] Visit this URL in your browser:
  ```
  https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
  ```
  (Replace `<YOUR_BOT_TOKEN>` with your actual bot token)
- [ ] Look for "chat" → "id" in the response
- [ ] Copy this number (your Chat ID)
- [ ] Save it safely

### Step 2: Install and Run

#### Using Docker (Recommended)
- [ ] Open terminal/command prompt
- [ ] Clone the repository:
  ```bash
  git clone https://github.com/sagipael/Ai-Travel-agent.git
  cd Ai-Travel-agent
  ```
- [ ] Set environment variables:
  
  **On Linux/Mac**:
  ```bash
  export GEMINI_API_TOKEN="your_token_here"
  export TELEGRAM_BOT_TOKEN="your_telegram_token"
  export TELEGRAM_CHAT_ID="your_chat_id"
  ```
  
  **On Windows (PowerShell)**:
  ```powershell
  $env:GEMINI_API_TOKEN="your_token_here"
  $env:TELEGRAM_BOT_TOKEN="your_telegram_token"
  $env:TELEGRAM_CHAT_ID="your_chat_id"
  ```

- [ ] Run the Docker container:
  ```bash
  docker run -p 5000:5000 \
    -e GEMINI_API_TOKEN=$GEMINI_API_TOKEN \
    -e TELEGRAM_BOT_TOKEN=$TELEGRAM_BOT_TOKEN \
    -e TELEGRAM_CHAT_ID=$TELEGRAM_CHAT_ID \
    my-ai-travel-agent:latest
  ```

- [ ] Wait for the container to start (should see "Running on http://0.0.0.0:5000")

### Step 3: Access the Application

- [ ] Open your web browser
- [ ] Navigate to: `http://localhost:5000`
- [ ] You should see the My AI Travel Agent dashboard
- [ ] If you see an error, check:
  - [ ] Docker container is running
  - [ ] Port 5000 is not used by another application
  - [ ] No firewall blocking the connection

## First Use Checklist

### Add Your First Destination

- [ ] Find the "Add Destination" section at the top
- [ ] Type a city name or airport code (try "Paris" or "CDG")
- [ ] Click the "Add Destination" button
- [ ] Your destination should appear in the list below
- [ ] If it doesn't work:
  - [ ] Check that you typed a valid city/airport code
  - [ ] Try a different destination
  - [ ] Refresh the page and try again

### Set Your Travel Dates

- [ ] Find the "Date Range" section
- [ ] Click on the "Departure Date" calendar
- [ ] Select a date (try a date 6-8 weeks from now)
- [ ] (Optional) Select a "Return Date" for round trip
- [ ] Click "Add Date Range"
- [ ] Your date range should appear in the list
- [ ] If it doesn't work:
  - [ ] Make sure departure is before return date
  - [ ] Try selecting dates again
  - [ ] Check that dates are in the future

### Start Monitoring

- [ ] Find the "Monitoring Settings" section
- [ ] Select check interval from dropdown
  - [ ] Recommended: "Every 6 hours" for first time
- [ ] Click "Start Monitoring" button
- [ ] Status should change to "🟢 Active"
- [ ] If it doesn't start:
  - [ ] Check that you have at least one destination
  - [ ] Check that you have at least one date range
  - [ ] Verify API credentials are correct
  - [ ] Check browser console for errors (F12)

### Verify Results

- [ ] Wait 1-2 minutes for first check to complete
- [ ] Scroll down to "Results" section
- [ ] You should see:
  - [ ] Your destination tab(s)
  - [ ] Current best price
  - [ ] "Last Updated" timestamp
- [ ] If no results appear:
  - [ ] Wait a bit longer (first check can take time)
  - [ ] Check monitoring status is "Active"
  - [ ] Verify internet connection
  - [ ] Check application logs

### Test Telegram Notifications

- [ ] Open Telegram app
- [ ] Find your bot in your chat list
- [ ] You should receive a welcome message when monitoring starts
- [ ] If no message:
  - [ ] Verify bot token is correct
  - [ ] Verify chat ID is correct
  - [ ] Make sure you sent /start to the bot
  - [ ] Check environment variables are set correctly

## Post-Setup Checklist

### Verify Everything is Working

- [ ] Dashboard loads correctly
- [ ] Can add/remove destinations
- [ ] Can add/remove date ranges
- [ ] Monitoring starts/stops correctly
- [ ] Results display after check completes
- [ ] Price graph shows data (after 2+ checks)
- [ ] Telegram notifications arrive
- [ ] Can navigate between destination tabs
- [ ] Can see price changes over time

### Optimize Your Settings

- [ ] Add 2-3 destinations for comparison
- [ ] Add 2-3 date ranges for flexibility
- [ ] Adjust check interval based on urgency
- [ ] Enable all notification types you want
- [ ] Set up daily summary (if desired)

### Bookmark Important Pages

- [ ] Bookmark the dashboard: `http://localhost:5000`
- [ ] Bookmark relevant documentation:
  - [ ] [Quick Reference](QUICK_REFERENCE.md)
  - [ ] [FAQ](FAQ.md)
  - [ ] [User Guide](USER_GUIDE.md)

## Learning Checklist

### Recommended Reading Order

- [ ] Read [README.md](README.md) for overview
- [ ] Complete [Quick Start Guide](HOW_TO_USE.md#quick-start-5-minutes)
- [ ] Review [Using the Price Graphs](HOW_TO_USE.md#using-the-price-graphs)
- [ ] Learn [Best Practices](USER_GUIDE.md#best-practices)
- [ ] Study [Understanding Results](USER_GUIDE.md#understanding-results)
- [ ] Check out [SCREENSHOTS.md](SCREENSHOTS.md) for UI reference
- [ ] Keep [QUICK_REFERENCE.md](QUICK_REFERENCE.md) handy
- [ ] Bookmark [FAQ.md](FAQ.md) for questions

### Practice Tasks

- [ ] Add and remove a destination
- [ ] Add multiple date ranges
- [ ] Change monitoring interval
- [ ] Stop and restart monitoring
- [ ] Navigate between destination tabs
- [ ] Read price graphs and trends
- [ ] Export data (if available)
- [ ] Respond to a Telegram notification

## Troubleshooting Checklist

If something isn't working:

### Basic Checks
- [ ] Is Docker running?
- [ ] Is the container running? (`docker ps`)
- [ ] Is the web page accessible?
- [ ] Is internet connected?
- [ ] Are environment variables set?
- [ ] Are API credentials valid?

### Common Issues
- [ ] No results showing → Wait longer, check monitoring status
- [ ] No Telegram notifications → Verify bot token and chat ID
- [ ] Prices outdated → Check "Last Updated" timestamp
- [ ] Graph not displaying → Wait for at least 2 checks
- [ ] Application slow → Reduce destinations or increase interval

### Where to Get Help
- [ ] Check [Troubleshooting Section](USER_GUIDE.md#troubleshooting)
- [ ] Review [Quick Troubleshooting](QUICK_REFERENCE.md#quick-troubleshooting)
- [ ] Read [FAQ Troubleshooting](FAQ.md#troubleshooting-questions)
- [ ] Open GitHub issue with details

## Success Checklist ✨

You're all set when you can:

- [x] Application is running
- [x] Dashboard is accessible
- [x] Destinations are added
- [x] Dates are configured
- [x] Monitoring is active
- [x] Results are displaying
- [x] Telegram notifications work
- [x] You understand the interface
- [x] You know where to find help

## Next Steps

Now that you're set up:

1. **Monitor for a few days** - Let the system collect data
2. **Watch the price trends** - Study the graphs
3. **Set up multiple destinations** - Compare options
4. **Enable all notifications** - Never miss a deal
5. **Book when ready** - Act on good deals quickly!

## Useful Resources

### Documentation
- [📖 README](README.md) - Project overview
- [🚀 How to Use](HOW_TO_USE.md) - Detailed guide
- [📚 User Guide](USER_GUIDE.md) - Complete manual
- [📋 Quick Reference](QUICK_REFERENCE.md) - Fast lookup
- [❓ FAQ](FAQ.md) - Common questions
- [🖼️ Screenshots](SCREENSHOTS.md) - UI reference

### External Resources
- [Docker Documentation](https://docs.docker.com/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Google AI Studio](https://makersuite.google.com/)

## Feedback

Help us improve this checklist:
- [ ] Was this checklist helpful?
- [ ] Did you encounter any issues not covered here?
- [ ] Are any steps unclear?
- [ ] Do you have suggestions?

Open a GitHub issue with your feedback!

---

**Congratulations!** You're ready to start finding great flight deals! ✈️

*Print this checklist and check off items as you complete them*

---

*Last Updated: February 2026*
