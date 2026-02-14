# 🛫 My AI Travel Agent

An intelligent travel agent powered by Google's Gemini AI that monitors flight prices and sends notifications via Telegram.

## Features

- 🤖 **AI-Powered Search**: Uses Gemini 2.0 Flash for intelligent flight price estimates and travel advice
- 📊 **Price Tracking**: Monitors flight prices at configurable intervals
- 📱 **Telegram Notifications**: Sends updates directly to your Telegram chat
- 📈 **Price Trends**: Visual charts showing price history over time
- 🌐 **User-Friendly Web UI**: Beautiful, responsive interface for managing searches
- 🐳 **Docker Support**: Easy deployment with Docker and Docker Compose
- ⚙️ **Automated CI/CD**: GitHub Actions workflow for automatic Docker image builds

## Quick Start

### Using Docker Compose (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/sagipael/Ai-Travel-agent.git
   cd Ai-Travel-agent
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

3. **Get your API keys**
   - **Gemini API Key**: Get from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - **Telegram Bot Token**: Create a bot using [@BotFather](https://t.me/botfather)
   - **Telegram Chat ID**: Get your chat ID from [@userinfobot](https://t.me/userinfobot)

4. **Run with Docker Compose**
   ```bash
   docker-compose up -d
   ```

5. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

### Using Docker

```bash
docker build -t ai-travel-agent .
docker run -p 5000:5000 \
  -e GEMINI_API_KEY="your_key" \
  -e TELEGRAM_BOT_TOKEN="your_token" \
  -e TELEGRAM_CHAT_ID="your_chat_id" \
  ai-travel-agent
```

### Manual Setup

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variables**
   ```bash
   export GEMINI_API_KEY="your_key"
   export TELEGRAM_BOT_TOKEN="your_token"
   export TELEGRAM_CHAT_ID="your_chat_id"
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

## Usage

1. **Open the Web UI** at `http://localhost:5000`

2. **Create a Search**:
   - Enter destinations (one per line)
   - Select date range for your trip
   - Choose check interval (how often to check prices)
   - Click "Start Monitoring"

3. **View Results**:
   - See all active searches
   - View recent price checks
   - Analyze price trends with interactive charts

4. **Receive Notifications**:
   - Get updates in your Telegram chat
   - Price alerts sent at configured intervals

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Google Gemini API key | Yes |
| `TELEGRAM_BOT_TOKEN` | Telegram bot token from @BotFather | Yes |
| `TELEGRAM_CHAT_ID` | Your Telegram chat ID | Yes |

## Architecture

- **Backend**: Python Flask with SQLite database
- **Frontend**: Vanilla JavaScript with Chart.js for visualizations
- **AI**: Google Gemini 2.0 Flash for intelligent search
- **Notifications**: Telegram Bot API
- **Scheduling**: APScheduler for periodic price checks
- **Containerization**: Docker with multi-stage builds
- **CI/CD**: GitHub Actions for automated builds

## API Endpoints

- `GET /` - Web UI
- `POST /api/search` - Create new flight search
- `GET /api/searches` - Get all active searches
- `DELETE /api/search/<id>` - Delete a search
- `GET /api/results` - Get all results
- `GET /api/chart/<destination>` - Get chart data for destination

## Development

### Project Structure
```
.
├── app.py                 # Flask application
├── templates/
│   └── index.html        # Web UI template
├── static/
│   ├── css/
│   │   └── style.css     # Styles
│   └── js/
│       └── app.js        # Frontend JavaScript
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
├── requirements.txt      # Python dependencies
└── .github/
    └── workflows/
        └── docker-build.yml  # CI/CD workflow
```

### Running Tests

```bash
# Install development dependencies
pip install -r requirements.txt

# Run the application in debug mode
python app.py
```

## Docker Hub

The Docker image is automatically built and published to Docker Hub via GitHub Actions on every push to the main branch.

To use the pre-built image:
```bash
docker pull <username>/ai-travel-agent:latest
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - feel free to use this project for any purpose.

## Acknowledgments

- Powered by Google Gemini AI
- Built with Flask and Chart.js
- Telegram integration for notifications