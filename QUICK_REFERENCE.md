# Quick Reference Guide

A one-page reference for common tasks in My AI Travel Agent.

## 🚀 Quick Start (60 Seconds)

1. Open: `http://localhost:5000`
2. Add destination: Type city name → Click "Add"
3. Select dates: Pick dates → Click "Add Range"
4. Start: Choose interval → Click "Start Monitoring"
5. Done! Check results below or wait for Telegram alerts

## 📋 Common Tasks

### Add a Destination
```
1. Type city or airport code (e.g., "Tokyo" or "NRT")
2. Click "Add Destination"
3. Destination appears in list
```

### Set Travel Dates
```
1. Click departure date calendar
2. Select date
3. (Optional) Select return date for round trip
4. Click "Add Date Range"
```

### Start Monitoring
```
1. Select check interval:
   - Every hour (urgent)
   - Every 6 hours (recommended)
   - Every 12 hours (normal)
   - Daily (long-term)
2. Click "Start Monitoring"
```

### View Results
```
1. Scroll to Results section
2. Click destination tabs to switch
3. View price graph and best price
4. Check "Last Updated" timestamp
```

### Remove a Destination
```
1. Find destination in list
2. Click [X] or "Remove" button
3. Confirm if prompted
```

## 🔔 Telegram Notifications

### Setup in 3 Steps
```
1. Message @BotFather on Telegram
   Send: /newbot
   Follow prompts → Get bot token

2. Get your Chat ID
   Start chat with your bot
   Visit: api.telegram.org/bot<TOKEN>/getUpdates
   Find "id" number

3. Configure app with:
   TELEGRAM_BOT_TOKEN=your_token
   TELEGRAM_CHAT_ID=your_chat_id
```

### Notification Types
- 🟢 Price Drop: When prices decrease
- ⭐ Best Deal: Exceptional prices found
- ⚠️ Price Increase: When prices go up
- 📊 Daily Summary: End of day recap

## 📊 Reading Price Graphs

### Graph Elements
- **Blue Line**: Price trend over time
- **Green Markers**: Price decreased
- **Red Markers**: Price increased
- **Dots**: Individual price checks

### Actions
- **Hover**: See exact price and time
- **Click & Drag**: Zoom into time period
- **Double Click**: Reset view

## 🎯 Best Practices

### For Best Deals
✅ Monitor 2-3 months before travel
✅ Add multiple date ranges
✅ Check weekday travel
✅ Compare nearby airports
✅ Set interval to every 6 hours
✅ Enable Telegram notifications

### When to Book
- Price significantly below average
- Downward trend starting to flatten
- 6-8 weeks before departure
- When you see "Best Deal" alert

## ⚙️ Settings Reference

### Check Intervals
| Interval | Use Case | Checks/Day |
|----------|----------|------------|
| Every hour | Urgent/last-minute | 24 |
| Every 6 hours | Recommended | 4 |
| Every 12 hours | Normal planning | 2 |
| Daily | Long-term monitoring | 1 |

### Recommended Setup
```
Destinations: 2-5 active
Date Ranges: 2-3 per destination
Check Interval: Every 6 hours
Notifications: Enabled
Monitoring: Always on
```

## 🆘 Quick Troubleshooting

### No Results Showing
→ Wait for first check cycle (based on interval)
→ Verify monitoring is started (green indicator)
→ Check internet connection

### No Telegram Notifications
→ Verify bot token and chat ID
→ Send /start to your bot in Telegram
→ Check environment variables

### Prices Seem Old
→ Check "Last Updated" timestamp
→ Verify monitoring status is "Active"
→ Consider shorter check interval

### Graph Not Loading
→ Refresh page (F5)
→ Wait for at least 2 price checks
→ Clear browser cache

## 📱 Mobile Tips

- Use landscape mode for better graph view
- Swipe between destination tabs
- Use browser's "Add to Home Screen"
- Enable push notifications in Telegram

## ⌨️ Keyboard Shortcuts

- `Tab` - Navigate between fields
- `Enter` - Submit/Add
- `Esc` - Close dialogs
- `F5` - Refresh page
- Arrow keys - Navigate graph (when focused)

## 💡 Pro Tips

1. **Compare Multiple Options**
   - Add 3-5 similar destinations
   - Add flexible date ranges
   - Let AI find best deal

2. **Set Target Prices**
   - Research average prices first
   - Know your budget
   - Book when target is met

3. **Use Price Trends**
   - Look for downward patterns
   - Don't wait for absolute bottom
   - Book when comfortable with price

4. **Flexible = Savings**
   - Wider date ranges = better deals
   - Weekday travel often cheaper
   - Off-peak seasons save money

## 🔗 Quick Links

- [Full User Guide](USER_GUIDE.md)
- [Step-by-Step How-To](HOW_TO_USE.md)
- [UI Screenshots](SCREENSHOTS.md)
- [README](README.md)

## 📞 Need Help?

1. Check this quick reference
2. Review full documentation
3. Look at troubleshooting section
4. Open GitHub issue

---

**Happy Price Hunting!** ✈️

*Print this page for easy reference while using the application*
