# My AI Travel Agent 🛫

An intelligent flight price monitoring tool powered by AI that helps you find the best deals for your travel plans.

## 📖 Documentation

### For End Users
- **[How to Use Guide](HOW_TO_USE.md)** - Quick start and step-by-step instructions
- **[User Guide](USER_GUIDE.md)** - Comprehensive guide with all features explained
- **[Screenshots & UI Guide](SCREENSHOTS.md)** - Visual guide to the interface

### Quick Links
- [Features](#features)
- [Getting Started](#getting-started)
- [How It Works](#how-it-works)
- [Configuration](#configuration)
- [Support](#support)

## ✨ Features

- 🔍 **Smart Price Monitoring**: Track flight prices across multiple destinations
- 📊 **Visual Analytics**: Interactive price graphs showing trends over time
- 🔔 **Telegram Alerts**: Instant notifications when prices drop
- 📅 **Flexible Dates**: Monitor multiple date ranges simultaneously
- 🤖 **AI-Powered**: Uses Gemini 2.5 Flash for intelligent price analysis
- 🌐 **Web Interface**: User-friendly dashboard for easy management
- ⏰ **Customizable Intervals**: Choose how often to check prices
- 📈 **Price History**: Track and compare prices over time

## 🚀 Getting Started

### Prerequisites
- Docker installed on your system
- Telegram account (for notifications)
- Gemini API token

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/sagipael/Ai-Travel-agent.git
cd Ai-Travel-agent
```

2. **Set up environment variables**
```bash
export GEMINI_API_TOKEN="your_gemini_token"
export TELEGRAM_BOT_TOKEN="your_telegram_bot_token"
export TELEGRAM_CHAT_ID="your_telegram_chat_id"
```

3. **Run with Docker**
```bash
docker run -p 5000:5000 \
  -e GEMINI_API_TOKEN=$GEMINI_API_TOKEN \
  -e TELEGRAM_BOT_TOKEN=$TELEGRAM_BOT_TOKEN \
  -e TELEGRAM_CHAT_ID=$TELEGRAM_CHAT_ID \
  my-ai-travel-agent:latest
```

4. **Access the web interface**
Open your browser and navigate to `http://localhost:5000`

For detailed instructions, see the [How to Use Guide](HOW_TO_USE.md).

## 🎯 How It Works

1. **Add Destinations**: Enter cities or airport codes you want to monitor
2. **Set Date Ranges**: Choose your travel dates (flexible options available)
3. **Start Monitoring**: Select check interval and activate monitoring
4. **Get Alerts**: Receive Telegram notifications when prices drop
5. **View Results**: Check interactive graphs and compare prices
6. **Book**: When you find a great deal, book directly through airlines

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_TOKEN` | Your Gemini AI API token | Yes |
| `TELEGRAM_BOT_TOKEN` | Telegram bot token for notifications | Yes |
| `TELEGRAM_CHAT_ID` | Your Telegram chat ID | Yes |
| `CHECK_INTERVAL` | Default check interval in hours | No (default: 6) |
| `PORT` | Web interface port | No (default: 5000) |

### Telegram Setup

1. Create a bot using [@BotFather](https://t.me/botfather) on Telegram
2. Get your bot token
3. Get your chat ID by messaging the bot and visiting:
   `https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates`

Detailed setup instructions are available in the [How to Use Guide](HOW_TO_USE.md#setting-up-telegram-notifications).

## 📱 Using the Application

### Adding Destinations
1. Enter city name or airport code (e.g., "Paris" or "CDG")
2. Click "Add Destination"
3. Repeat for multiple destinations

### Setting Date Ranges
1. Select departure date
2. (Optional) Select return date for round trips
3. Click "Add Date Range"
4. Add multiple ranges for flexibility

### Monitoring
1. Choose check interval from dropdown
2. Click "Start Monitoring"
3. View results in the dashboard
4. Receive Telegram alerts for price changes

For complete instructions with screenshots, see:
- [How to Use Guide](HOW_TO_USE.md) - Step-by-step instructions
- [Screenshots Guide](SCREENSHOTS.md) - Visual UI reference

## 📊 Understanding Results

The results dashboard shows:
- **Price Graphs**: Visual trends over time
- **Best Prices**: Highlighted lowest fares
- **Price Changes**: Up/down indicators
- **Statistics**: Average, highest, lowest prices
- **Recommendations**: AI-powered booking suggestions

See the [User Guide](USER_GUIDE.md#understanding-results) for detailed explanations.

## 🆘 Support

### Documentation
- [User Guide](USER_GUIDE.md) - Complete feature documentation
- [How to Use](HOW_TO_USE.md) - Step-by-step tutorials
- [Screenshots](SCREENSHOTS.md) - UI visual reference

### Troubleshooting
Common issues and solutions are documented in the [User Guide Troubleshooting Section](USER_GUIDE.md#troubleshooting).

### Getting Help
- Check the documentation first
- Review common issues in the User Guide
- Open an issue on GitHub for bugs or feature requests

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Powered by Google Gemini AI
- Built with Flask and modern web technologies
- Telegram Bot API for notifications

---

**Ready to save on flights?** Check out the [How to Use Guide](HOW_TO_USE.md) to get started! ✈️