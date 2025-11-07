"""
Configuration for City Guardian Bot
"""

# API Configuration
API_BASE_URL = "https://api.raipurmunicipal.gov.in"  # Example URL
API_KEY = None  # Set your API key here or use environment variable

# Bot Configuration
BOT_NAME = "City Guardian"
SUPPORTED_LANGUAGES = ["hi", "en"]  # Hindi, English

# Complaint ID Pattern
COMPLAINT_ID_PATTERN = r'CG-\d{4}-\d{5}'

# Environmental Thresholds (for advisories)
THRESHOLDS = {
    'aqi': {
        'good': 50,
        'moderate': 100,
        'unhealthy_sensitive': 150,
        'unhealthy': 200,
        'very_unhealthy': 300
    },
    'pm25': {
        'target': 40.0,  # µg/m³
        'critical': 100.0
    },
    'noise': {
        'day_limit': 65.0,  # dB
        'night_limit': 55.0
    }
}

# Response Templates
REDIRECT_COMPLAINT_REGISTRATION = {
    'hi': "Aapki shikayat darj karne ke liye, kripya dedicated 'Complaint Registration' page ka upyog karen. Main yahan support aur status update ke liye hoon.",
    'en': "To register your complaint, please use the dedicated 'Complaint Registration' page. I am here for support and status updates."
}

# Complaint Status Mapping
STATUS_DISPLAY = {
    'REGISTERED': {'hi': 'Darj', 'en': 'Registered'},
    'TEAM_ASSIGNED': {'hi': 'Team Niyukt', 'en': 'Team Assigned'},
    'IN_PROGRESS': {'hi': 'Kaam Jari Hai', 'en': 'In Progress'},
    'RESOLVED': {'hi': 'Samadhan Ho Gaya', 'en': 'Resolved'},
    'PENDING_REVIEW': {'hi': 'Samiksha Lambit', 'en': 'Pending Supervisor Review'}
}

# AQI Categories
AQI_CATEGORIES = {
    'good': {'hi': 'Accha', 'en': 'Good'},
    'moderate': {'hi': 'Madhyam', 'en': 'Moderate'},
    'unhealthy_sensitive': {'hi': 'Sanvedanshil Logon Ke Liye Hanikarak', 'en': 'Unhealthy for Sensitive Groups'},
    'unhealthy': {'hi': 'Hanikarak', 'en': 'Unhealthy'},
    'very_unhealthy': {'hi': 'Bahut Hanikarak', 'en': 'Very Unhealthy'},
    'hazardous': {'hi': 'Khatarnak', 'en': 'Hazardous'}
}
