# City Guardian AI Assistant 🏛️

AI-powered chatbot for Raipur Municipal Corporation support interface, designed to provide citizens with information about municipal services, complaint tracking, environmental data, and policy information.

## 🎯 Features

### Core Capabilities

1. **Complaint Status & Support** 📋
   - Track complaint status using Complaint ID
   - Get real-time updates on assigned teams and resolution timelines
   - View zone and team assignments

2. **Environmental Data Summary** 🌍
   - Access AQI (Air Quality Index) data
   - Monitor PM2.5, humidity, wind speed, and other environmental metrics
   - Receive advisories when pollution thresholds are breached

3. **Policy & Schemes Information** 📚
   - Learn about municipal policies and schemes
   - Get step-by-step procedures for services
   - Access required documents and forms

4. **Zone Achievements & Milestones** 🏆
   - View top-performing zones
   - Track improvements in environmental metrics
   - Celebrate municipal achievements

### Key Features

- **Bilingual Support**: Hindi & English (automatic detection)
- **Smart Intent Detection**: Automatically understands user queries
- **API Integration**: Connects to municipal service APIs
- **Complaint Registration Prevention**: Redirects users to proper complaint registration page

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/ashishbalodia1/Chat-Bot.git
cd Chat-Bot

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```python
from city_guardian_bot import CityGuardianBot
from api_client import MockAPIClient

# Initialize bot with mock API client
api_client = MockAPIClient()
bot = CityGuardianBot(api_client=api_client)

# Process a message
response = bot.process_message("Meri complaint ID CG-2025-00045 ki status batao")
print(response)
```

### Interactive Mode

```bash
python city_guardian_bot.py
```

## 📖 Usage Examples

### Example 1: Check Complaint Status (Hindi)
```
User: "Meri complaint ID CG-2025-00045 ki status batao."
Bot: "Complaint CG-2025-00045: Team Assigned (Zone 4 - Sewage Unit). Status: In Progress. Expected resolution: 3 days."
```

### Example 2: Environmental Data (Hindi)
```
User: "Zone 3 ka AQI kaisa hai aaj?"
Bot: "Zone 3 — AQI: 172 (Unhealthy). PM2.5: 95 µg/m³ — target < 40 µg/m³. Advisory: Bahar exercise se bachen; vulnerable logo ke liye mask ki sifaarish."
```

### Example 3: Complaint Registration Redirect (Hindi)
```
User: "Main nayi shikayat darj karna chahta hoon"
Bot: "Aapki shikayat darj karne ke liye, kripya dedicated 'Complaint Registration' page ka upyog karen. Main yahan support aur status update ke liye hoon."
```

### Example 4: Zone Achievements (English)
```
User: "Show me the top performing zones"
Bot: "Top Zones: Zone 2 (15% improvement in PM2.5), Zone 5 (95% success in complaint resolution). Congratulations!"
```

## 🔌 API Integration

The bot integrates with the following municipal APIs:

### 1. Complaint Status API
```
GET /complaint/status?id=[ID]
```

### 2. Environmental Data API
```
GET /environment/data?zone=[ZoneID]
```

### 3. Performance Rankings API
```
GET /performance/rankings
```

### Configuration

Edit `config.py` to set your API endpoint and credentials:

```python
API_BASE_URL = "https://api.raipurmunicipal.gov.in"
API_KEY = "your-api-key-here"
```

## 🏗️ Architecture

```
city_guardian_bot.py    # Main bot logic and intent detection
├── Intent Detection    # Classify user queries
├── Language Detection  # Hindi/English detection
├── Response Handlers   # Generate appropriate responses
└── API Integration     # Fetch data from municipal APIs

api_client.py          # API client for external services
├── MunicipalAPIClient # Real API client
└── MockAPIClient      # Mock client for testing

config.py              # Configuration and constants
```

## 🔒 Constraints & Security

- **No Direct Complaint Registration**: The bot never registers complaints directly. It always redirects users to the dedicated complaint registration page.
- **Privacy First**: Does not ask for excessive personal data
- **No Legal/Medical Advice**: Provides only basic informational guidance
- **API Authentication**: Uses secure API keys for all external calls

## 🌐 Supported Languages

- **Hindi (हिंदी)**: Primary language for local citizens
- **English**: For broader accessibility

The bot automatically detects the language based on user input and responds accordingly.

## 📝 Response Guidelines

The bot follows these principles:
- **Concise**: 2-5 sentences maximum
- **Actionable**: Includes next steps or links
- **Professional**: Helpful and respectful tone
- **Accurate**: Real-time data from municipal APIs
- **Bilingual**: Responds in user's language

## 🤖 Bot Persona

**Name**: City Guardian  
**Role**: Municipal Support Assistant  
**Tone**: Professional, helpful, accurate, and encouraging  
**Goal**: Provide accurate, real-time information about municipal services

## 🧪 Testing

The project includes a `MockAPIClient` for testing without connecting to real APIs:

```python
from city_guardian_bot import CityGuardianBot
from api_client import MockAPIClient

# Use mock client for testing
bot = CityGuardianBot(api_client=MockAPIClient())
```

## 📄 License

This project is licensed under the terms specified in the LICENSE file.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📧 Contact

For questions or support, please contact the Raipur Municipal Corporation IT department.

---

**Built with ❤️ for Raipur Municipal Corporation**
