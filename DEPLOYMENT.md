# Deployment Guide for City Guardian AI Assistant

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ashishbalodia1/Chat-Bot.git
cd Chat-Bot
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configuration

Edit `config.py` to set your API endpoints:

```python
API_BASE_URL = "https://api.raipurmunicipal.gov.in"
API_KEY = "your-api-key-here"
```

Or use environment variables:

```bash
export MUNICIPAL_API_URL="https://api.raipurmunicipal.gov.in"
export MUNICIPAL_API_KEY="your-api-key"
```

### 5. Run Tests

```bash
python test_bot.py
```

All tests should pass (21/21).

## Running the Application

### Option 1: Command Line Interface

```bash
python city_guardian_bot.py
```

This starts an interactive chat session.

### Option 2: Example Demonstrations

```bash
# Run pre-defined examples
python examples.py

# Run in interactive mode
python examples.py --interactive
```

### Option 3: Web Server (API)

```bash
python app.py
```

The server will start on `http://localhost:5000`

#### API Endpoints:

- `GET /health` - Health check
- `POST /chat` - Send message to chatbot
- `GET /status/<complaint_id>` - Get complaint status
- `GET /environment/<zone_id>` - Get environmental data
- `GET /performance` - Get performance rankings

#### Example API Usage:

```bash
# Health check
curl http://localhost:5000/health

# Send chat message
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Meri complaint ID CG-2025-00045 ki status batao"}'
```

### Option 4: Web Interface

1. Start the web server:
```bash
python app.py
```

2. Open `index.html` in a web browser

3. Start chatting with the City Guardian bot!

Note: You may need to update the `API_URL` in `index.html` if your server is running on a different port or host.

## Production Deployment

### Using Gunicorn (Recommended)

1. Install Gunicorn:
```bash
pip install gunicorn
```

2. Run the application:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

Options:
- `-w 4`: Run with 4 worker processes
- `-b 0.0.0.0:5000`: Bind to all interfaces on port 5000

### Using Docker

Create a `Dockerfile`:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

Build and run:

```bash
docker build -t city-guardian-bot .
docker run -p 5000:5000 -e MUNICIPAL_API_KEY=your-key city-guardian-bot
```

### Environment Variables

Set these environment variables for production:

```bash
MUNICIPAL_API_URL=https://api.raipurmunicipal.gov.in
MUNICIPAL_API_KEY=your-secure-api-key
PORT=5000
DEBUG=False
```

### Nginx Reverse Proxy

Example Nginx configuration:

```nginx
server {
    listen 80;
    server_name cityguardian.raipurmunicipal.gov.in;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

## Monitoring & Logging

### Application Logs

The Flask application logs to stdout by default. In production, redirect logs to a file:

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app --access-logfile access.log --error-logfile error.log
```

### Health Monitoring

Monitor the `/health` endpoint to ensure the service is running:

```bash
curl http://localhost:5000/health
```

Expected response:
```json
{
  "status": "healthy",
  "service": "City Guardian AI Assistant",
  "version": "1.0.0"
}
```

## Security Considerations

1. **API Keys**: Never commit API keys to version control. Use environment variables.

2. **HTTPS**: Always use HTTPS in production. Configure SSL/TLS certificates.

3. **Rate Limiting**: Implement rate limiting to prevent abuse:
   ```bash
   pip install flask-limiter
   ```

4. **Input Validation**: The bot validates all inputs, but ensure your API endpoints also validate data.

5. **CORS**: Adjust CORS settings in `app.py` for your specific domain:
   ```python
   CORS(app, origins=["https://yourdomain.com"])
   ```

## Troubleshooting

### Issue: Bot not responding
- Check if the server is running: `curl http://localhost:5000/health`
- Verify API credentials are set correctly
- Check logs for errors

### Issue: Tests failing
- Ensure you're in the correct directory
- Check Python version: `python --version` (should be 3.8+)
- Reinstall dependencies: `pip install -r requirements.txt`

### Issue: API errors
- Verify API endpoints are accessible
- Check API key is valid
- Use MockAPIClient for testing: The bot falls back to mock data if no API key is provided

## Scaling

For high traffic deployments:

1. **Horizontal Scaling**: Run multiple instances behind a load balancer
2. **Caching**: Implement Redis caching for frequent queries
3. **Database**: Store conversation history if needed
4. **CDN**: Serve static files (HTML, CSS, JS) via CDN

## Support

For issues or questions:
- Create an issue on GitHub
- Contact: Raipur Municipal Corporation IT Department
- Email: support@raipurmunicipal.gov.in

## License

See LICENSE file for details.
