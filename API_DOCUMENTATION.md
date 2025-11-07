# API Documentation - City Guardian AI Assistant

## Overview

The City Guardian AI Assistant provides a REST API for integration with web and mobile applications. The API supports bilingual communication (Hindi & English) and provides access to municipal services information.

## Base URL

```
http://localhost:5000  (Development)
https://api.cityguardian.raipurmunicipal.gov.in  (Production)
```

## Authentication

For production deployments, API endpoints require authentication via API key:

```
Authorization: Bearer YOUR_API_KEY
```

## Endpoints

### 1. Health Check

Check if the service is running.

**Endpoint:** `GET /health`

**Response:**
```json
{
  "status": "healthy",
  "service": "City Guardian AI Assistant",
  "version": "1.0.0"
}
```

**Status Codes:**
- `200 OK` - Service is healthy

---

### 2. Chat Message

Send a message to the chatbot and receive a response.

**Endpoint:** `POST /chat`

**Request Body:**
```json
{
  "message": "Meri complaint ID CG-2025-00045 ki status batao"
}
```

**Response:**
```json
{
  "response": "Complaint CG-2025-00045: Team Assigned (Zone 4 - Sewage Unit). Current status: In Progress. Expected resolution: 3 days.",
  "language": "hi",
  "bot_name": "City Guardian"
}
```

**Parameters:**
- `message` (string, required) - User's message in Hindi or English

**Response Fields:**
- `response` (string) - Bot's response message
- `language` (string) - Detected language (`hi` for Hindi, `en` for English)
- `bot_name` (string) - Name of the bot

**Status Codes:**
- `200 OK` - Successful response
- `400 Bad Request` - Missing or invalid message
- `500 Internal Server Error` - Server error

**Example Usage:**

```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is the AQI in Zone 3?"}'
```

**Example Queries:**

Hindi:
- `"Meri complaint ID CG-2025-00045 ki status batao"`
- `"Zone 3 ka AQI kaisa hai?"`
- `"Sabse achhe zones kaun se hain?"`

English:
- `"What is the status of complaint CG-2025-12345?"`
- `"Show me environmental data for Zone 2"`
- `"Tell me about top performing zones"`

---

### 3. Complaint Status

Get the status of a specific complaint.

**Endpoint:** `GET /status/<complaint_id>`

**Path Parameters:**
- `complaint_id` (string, required) - Complaint ID (format: CG-YYYY-NNNNN)

**Response:**
```json
{
  "complaint_id": "CG-2025-00045",
  "status": "In Progress",
  "status_code": "IN_PROGRESS",
  "zone": "4",
  "team": "Sewage Unit",
  "estimated_resolution_days": 3,
  "details": "Team has been assigned and work is in progress",
  "created_at": "2025-11-01T10:00:00Z",
  "last_updated": "2025-11-05T14:30:00Z"
}
```

**Status Codes:**
- `200 OK` - Successful response
- `404 Not Found` - Complaint ID not found
- `500 Internal Server Error` - Server error

**Example Usage:**

```bash
curl http://localhost:5000/status/CG-2025-00045
```

**Status Values:**
- `REGISTERED` - Complaint has been registered
- `TEAM_ASSIGNED` - Team has been assigned to the complaint
- `IN_PROGRESS` - Work is in progress
- `RESOLVED` - Complaint has been resolved
- `PENDING_REVIEW` - Pending supervisor review

---

### 4. Environmental Data

Get environmental data for a specific zone.

**Endpoint:** `GET /environment/<zone_id>`

**Path Parameters:**
- `zone_id` (string, required) - Zone identifier (e.g., "1", "2", "3")

**Response:**
```json
{
  "zone": "3",
  "aqi": 172,
  "aqi_category": "Unhealthy",
  "pm25": 95.0,
  "pm25_target": 40.0,
  "humidity": 65.0,
  "wind_speed": 12.5,
  "wind_direction": "NE",
  "noise_level": 75.0,
  "temperature": 28.5,
  "advisory": "Avoid outdoor exercise; masks recommended for vulnerable people",
  "measured_at": "2025-11-07T10:00:00Z"
}
```

**Status Codes:**
- `200 OK` - Successful response
- `404 Not Found` - Zone not found
- `500 Internal Server Error` - Server error

**Example Usage:**

```bash
curl http://localhost:5000/environment/3
```

**AQI Categories:**
- `0-50` - Good
- `51-100` - Moderate
- `101-150` - Unhealthy for Sensitive Groups
- `151-200` - Unhealthy
- `201-300` - Very Unhealthy
- `301+` - Hazardous

---

### 5. Performance Rankings

Get performance rankings and achievements for zones.

**Endpoint:** `GET /performance`

**Response:**
```json
{
  "top_zones": [
    {
      "zone": "2",
      "rank": 1,
      "metric": "PM2.5 Improvement",
      "value": "15%",
      "score": 95
    },
    {
      "zone": "5",
      "rank": 2,
      "metric": "Complaint Resolution",
      "value": "95%",
      "score": 92
    }
  ],
  "recent_achievements": [
    "Zone 2 reduced PM2.5 levels by 15% in last quarter",
    "Zone 5 achieved 95% complaint resolution rate",
    "Zone 1 completed 100% garbage collection efficiency"
  ],
  "generated_at": "2025-11-07T10:00:00Z"
}
```

**Status Codes:**
- `200 OK` - Successful response
- `500 Internal Server Error` - Server error

**Example Usage:**

```bash
curl http://localhost:5000/performance
```

---

## Bot Capabilities

### Intent Detection

The bot automatically detects the following intents:

1. **Complaint Status** - Track existing complaints
   - Keywords: status, track, complaint id, shikayat ka status
   - Example: "What is the status of CG-2025-00045?"

2. **Environmental Data** - Get environmental metrics
   - Keywords: AQI, air quality, pollution, PM2.5, environment
   - Example: "Zone 3 ka AQI kaisa hai?"

3. **Achievements** - View zone performance
   - Keywords: achievement, milestone, ranking, top zone
   - Example: "Show me top performing zones"

4. **Policy Information** - Learn about municipal policies
   - Keywords: policy, scheme, process, procedure
   - Example: "How to apply for water connection?"

5. **Complaint Registration** - Redirects to complaint page
   - Keywords: register complaint, new complaint, nayi shikayat
   - Action: Redirects user to dedicated complaint registration page

### Language Detection

The bot automatically detects the user's language:
- Detects Hindi if Devanagari script is present
- Defaults to English otherwise
- Responds in the same language as the user

## Error Handling

All endpoints return appropriate HTTP status codes and error messages:

**400 Bad Request:**
```json
{
  "error": "Missing message in request body"
}
```

**404 Not Found:**
```json
{
  "error": "Complaint ID not found"
}
```

**500 Internal Server Error:**
```json
{
  "error": "Failed to fetch complaint status: Connection timeout"
}
```

## Rate Limiting

To prevent abuse, implement rate limiting in production:
- Default: 100 requests per minute per IP
- Burst: 10 requests per second

## CORS

Cross-Origin Resource Sharing (CORS) is enabled for web applications. Configure allowed origins in production:

```python
CORS(app, origins=["https://yourdomain.com"])
```

## WebSocket Support (Future)

For real-time chat, WebSocket support can be added:
- Endpoint: `ws://localhost:5000/ws/chat`
- Benefits: Real-time bidirectional communication
- Use case: Live chat interface

## Integration Examples

### JavaScript (Fetch API)

```javascript
async function sendMessage(message) {
  const response = await fetch('http://localhost:5000/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ message: message })
  });
  
  const data = await response.json();
  return data.response;
}

// Usage
const reply = await sendMessage('Zone 3 ka AQI batao');
console.log(reply);
```

### Python (requests)

```python
import requests

def send_message(message):
    url = 'http://localhost:5000/chat'
    response = requests.post(url, json={'message': message})
    return response.json()['response']

# Usage
reply = send_message('What is the status of CG-2025-00045?')
print(reply)
```

### cURL

```bash
# Chat message
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Show me environmental data for Zone 2"}'

# Complaint status
curl http://localhost:5000/status/CG-2025-00045

# Environmental data
curl http://localhost:5000/environment/3

# Performance rankings
curl http://localhost:5000/performance
```

## Testing

Use the MockAPIClient for testing without connecting to real APIs:

```python
from city_guardian_bot import CityGuardianBot
from api_client import MockAPIClient

bot = CityGuardianBot(api_client=MockAPIClient())
response = bot.process_message("Test message")
```

## Support

For API support:
- GitHub Issues: https://github.com/ashishbalodia1/Chat-Bot/issues
- Email: support@raipurmunicipal.gov.in
- Documentation: See README.md and DEPLOYMENT.md

## Changelog

### Version 1.0.0 (2025-11-07)
- Initial release
- Bilingual support (Hindi & English)
- Complaint status tracking
- Environmental data summaries
- Performance rankings
- Policy information
- Complaint registration prevention
