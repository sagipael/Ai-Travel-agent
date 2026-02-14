# Frequently Asked Questions (FAQ)

Common questions and answers about My AI Travel Agent.

## General Questions

### What is My AI Travel Agent?
My AI Travel Agent is an intelligent flight price monitoring tool that uses AI (Gemini 2.5 Flash) to track flight prices across multiple destinations and date ranges. It sends you notifications when prices drop and provides visual analytics to help you find the best deals.

### Is it free to use?
Yes, the application itself is free and open-source. However, you'll need:
- A Gemini API token (may have usage costs depending on your plan)
- A Telegram account (free)
- Internet connection

### Do I need coding knowledge to use it?
No! The application is designed for end users with a simple web interface. Just open your browser and start using it. Technical setup (Docker, environment variables) may require basic command-line knowledge.

### Which platforms are supported?
The application runs in Docker, which means it works on:
- Windows (with Docker Desktop)
- macOS (with Docker Desktop)
- Linux (native Docker support)

Access the web interface from any modern browser (Chrome, Firefox, Safari, Edge).

## Setup Questions

### How do I get a Gemini API token?
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Get API Key"
4. Copy your API key and use it as GEMINI_API_TOKEN

### How do I set up Telegram notifications?
See the detailed guide in [HOW_TO_USE.md - Setting Up Telegram Notifications](HOW_TO_USE.md#setting-up-telegram-notifications).

Quick steps:
1. Message @BotFather on Telegram
2. Create a new bot with /newbot
3. Get your bot token
4. Start your bot and get your chat ID
5. Configure environment variables

### What are the system requirements?
**Minimum**:
- 2GB RAM
- 1 CPU core
- 1GB disk space
- Internet connection

**Recommended**:
- 4GB RAM
- 2 CPU cores
- 5GB disk space
- Stable internet connection

### Can I run this on a cloud server?
Yes! The application works great on cloud servers like AWS, Google Cloud, Azure, or DigitalOcean. This allows 24/7 monitoring without keeping your computer on.

## Usage Questions

### How many destinations can I monitor?
Technically unlimited, but we recommend:
- **3-5 destinations** for optimal performance
- **Up to 10** if you have good resources
- Each destination requires API calls for price checking

### What destinations are supported?
Any destination served by commercial airlines:
- International flights
- Domestic flights
- Major cities and airports worldwide

Enter city names (e.g., "Paris") or airport codes (e.g., "CDG").

### Can I search for one-way flights?
Yes! When setting date ranges, simply:
1. Select departure date
2. Leave return date empty
3. Add the date range

### How accurate are the prices?
Prices are fetched in real-time and are generally accurate. However:
- Final prices may include additional fees/taxes
- Prices can change rapidly
- Always verify on the airline's website before booking

### How often should I check prices?
**Recommendations**:
- **Every 6 hours**: Best balance for most users
- **Every hour**: For urgent/last-minute travel
- **Daily**: For long-term planning (3+ months out)
- **Every 12 hours**: For casual monitoring

### When is the best time to book?
Based on general trends:
- **Domestic flights**: 4-6 weeks before departure
- **International flights**: 8-12 weeks before departure
- **Off-season**: Can book closer to dates
- **Peak season**: Book as early as possible

Watch the price graphs to identify good booking windows for your specific route.

## Features Questions

### What do the price alerts mean?
**Alert Types**:
- 🟢 **Price Drop**: Price decreased since last check
- ⭐ **Best Deal**: AI identified exceptional price (15%+ below average)
- ⚠️ **Price Increase**: Price went up
- 📊 **Daily Summary**: Overview of all monitored flights

### How does the AI help?
The AI (Gemini 2.5 Flash):
- Analyzes price patterns and trends
- Identifies unusually good deals
- Provides booking recommendations
- Learns from historical data
- Compares prices across dates and destinations

### Can I export my data?
Yes, you can export:
- CSV files with price history
- PDF reports (coming soon)
- Graph images (screenshot)

Look for the "Export" button in the Results section.

### Can I share my searches with others?
Currently, each instance is designed for single-user use. To share:
- Export data and send to others
- Share screenshots of graphs
- Multiple users can run their own instances

## Technical Questions

### Why use Docker?
Docker provides:
- Easy setup and deployment
- Consistent environment across platforms
- Isolation from your system
- Easy updates
- Portability to any server

### How much data does it use?
Approximate data usage:
- Per check: ~1-5 MB depending on destinations
- Daily (4 checks): ~4-20 MB
- Monthly: ~120-600 MB

With 3 destinations and 6-hour checks.

### Can I use it without Telegram?
Technically yes, but you'll miss notifications. Telegram is highly recommended for:
- Instant price drop alerts
- Best deal notifications
- Daily summaries
- System status updates

### Is my data secure?
Yes:
- All data stored locally in your Docker container
- No data sent to third parties (except flight APIs)
- Telegram Chat ID used only for notifications
- No personal information collected
- Open-source code - verify yourself

### Can I run multiple instances?
Yes, but consider:
- Each instance needs its own port
- Each needs separate Telegram bot (optional)
- Each uses system resources
- API rate limits may apply

## Price & Booking Questions

### Does this book flights for me?
No, the application only monitors and tracks prices. To book:
1. Click "Book Now" button in results
2. You'll be directed to airline or booking site
3. Complete booking there

### Why don't you book directly?
We focus on price monitoring and deal finding. Booking requires:
- Payment processing
- Legal compliance
- Customer support infrastructure
- Partnership agreements

We provide the best prices; you book at your preferred site.

### Are there hidden fees?
The application shows base fares. Airlines may add:
- Baggage fees
- Seat selection fees
- Taxes and airport fees
- Booking fees

Always check final price before booking.

### Can I get refunds through you?
No, we don't process bookings. For refunds:
- Contact the airline or booking site
- Follow their refund policy
- We only monitor prices

## Troubleshooting Questions

### Why aren't prices updating?
Check:
- ✅ Is monitoring active? (green status)
- ✅ Is interval set correctly?
- ✅ Has enough time passed for next check?
- ✅ Is internet connected?
- ✅ Are API credentials valid?

### No Telegram notifications?
Verify:
- ✅ Bot token is correct
- ✅ Chat ID is correct
- ✅ You sent /start to the bot
- ✅ Bot is not blocked
- ✅ Environment variables are set

### Prices seem wrong or outdated?
Possible reasons:
- API data delay (can be 15-30 minutes old)
- Currency conversion issues
- Cached data (try refreshing)
- Check "Last Updated" timestamp

See full troubleshooting guide: [USER_GUIDE.md - Troubleshooting](USER_GUIDE.md#troubleshooting)

## Privacy Questions

### What information do you collect?
We only store:
- Your search preferences (destinations, dates)
- Price history for your searches
- Telegram Chat ID (for notifications)

We do NOT collect:
- Personal identification
- Payment information
- Browsing history
- Email addresses
- Phone numbers

### Can others see my searches?
No, each instance is private. Your searches are:
- Stored locally in your container
- Not shared with other users
- Not visible to others
- Cleared if you delete the container

### Is my Telegram chat private?
Yes:
- Only you receive notifications
- Your Chat ID is used only for messaging
- No one else can intercept messages
- Standard Telegram encryption applies

## Advanced Questions

### Can I customize the check intervals?
Yes, you can set:
- Predefined intervals (hourly, 6h, 12h, daily)
- Custom intervals via configuration
- Different intervals per destination (advanced)

### Can I set price alerts?
You can:
- Enable automatic best deal alerts
- Configure threshold for notifications
- Set target prices (coming soon)
- Custom alert rules (advanced configuration)

### Does it support multiple currencies?
Currently shows prices in the default currency from the flight API. Multi-currency support is planned for future versions.

### Can I add filters (stops, airlines, times)?
Basic version monitors all flights. Advanced filters planned:
- Maximum stops
- Preferred airlines
- Time of day preferences
- Maximum duration

### Is there an API?
Not currently, but planned for future versions. This would allow:
- Integration with other tools
- Custom automation
- Third-party apps
- Advanced analytics

## Getting Help

### Where can I find more help?
1. **Documentation**:
   - [User Guide](USER_GUIDE.md) - Complete guide
   - [How to Use](HOW_TO_USE.md) - Step-by-step
   - [Screenshots](SCREENSHOTS.md) - Visual reference
   - [Quick Reference](QUICK_REFERENCE.md) - Fast lookup

2. **GitHub**:
   - Check existing issues
   - Open new issue for bugs
   - Request features
   - View source code

3. **Community**:
   - GitHub Discussions (if available)
   - Share tips and tricks
   - Help other users

### How do I report a bug?
1. Check if it's a known issue
2. Gather information:
   - Error messages
   - Steps to reproduce
   - Screenshots
   - Log files
3. Open a GitHub issue with details

### How do I request a feature?
1. Check if it's already requested
2. Open a GitHub issue
3. Describe the feature
4. Explain use case
5. Community can vote on it

### Can I contribute?
Yes! Contributions welcome:
- Code improvements
- Documentation updates
- Bug fixes
- Feature additions
- Translations
- UI improvements

See CONTRIBUTING.md (if available) for guidelines.

## Best Practices

### How can I save the most money?
Tips for maximum savings:
1. ✈️ **Be flexible**: Wider date ranges = better deals
2. 📅 **Book early**: 6-8 weeks optimal for most routes
3. 🌍 **Compare destinations**: Similar places, different prices
4. 📊 **Watch trends**: Use graphs to time your booking
5. ⏰ **Monitor early**: Start 2-3 months before travel
6. 🔔 **Enable alerts**: Never miss a deal
7. ✅ **Act fast**: Great deals don't last

### What mistakes should I avoid?
❌ **Don't**:
- Wait for absolute lowest price (may never come)
- Monitor too many destinations (slows system)
- Check too frequently (wastes resources)
- Ignore the price graphs
- Miss notification opportunities
- Book without verifying final price
- Forget about additional fees

### Pro tips from experienced users
💡 **Pro Tips**:
- Compare nearby airports (can save 30-50%)
- Tuesday/Wednesday often cheapest
- Set up multiple date ranges
- Use one-way prices for round trips sometimes
- Clear dates in price calendar
- Book separate tickets for multi-city
- Mix airlines for best overall price

---

## Still have questions?

- 📖 Read the [User Guide](USER_GUIDE.md)
- 🚀 Check [How to Use](HOW_TO_USE.md)
- 🖼️ View [Screenshots](SCREENSHOTS.md)
- 📋 Use [Quick Reference](QUICK_REFERENCE.md)
- 🐛 Open an issue on GitHub
- 💬 Ask in GitHub Discussions

**Can't find your answer?** Open a GitHub issue with your question!

---

*Last Updated: February 2026*
