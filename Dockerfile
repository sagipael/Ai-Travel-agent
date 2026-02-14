FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .
COPY templates/ ./templates/
COPY static/ ./static/

# Create directory for database
RUN mkdir -p /app/data

# Expose port
EXPOSE 5000

# Environment variables (to be set at runtime)
ENV GEMINI_API_KEY=""
ENV TELEGRAM_BOT_TOKEN=""
ENV TELEGRAM_CHAT_ID=""

# Run the application
CMD ["python", "app.py"]
