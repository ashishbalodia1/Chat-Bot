"""
Flask Web Server for City Guardian AI Assistant
Provides REST API endpoint for chatbot integration
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from city_guardian_bot import CityGuardianBot
from api_client import MockAPIClient, MunicipalAPIClient
import config
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for web integration

# Initialize bot
api_key = os.environ.get('MUNICIPAL_API_KEY', config.API_KEY)
base_url = os.environ.get('MUNICIPAL_API_URL', config.API_BASE_URL)

# Use mock client if no API key is provided
if api_key:
    api_client = MunicipalAPIClient(base_url, api_key)
else:
    api_client = MockAPIClient()

bot = CityGuardianBot(api_client=api_client)


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'City Guardian AI Assistant',
        'version': '1.0.0'
    })


@app.route('/chat', methods=['POST'])
def chat():
    """
    Main chat endpoint
    
    Request body:
    {
        "message": "user message text"
    }
    
    Response:
    {
        "response": "bot response text",
        "language": "hi" or "en"
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({
                'error': 'Missing message in request body'
            }), 400
        
        user_message = data['message']
        
        # Process message through bot
        response = bot.process_message(user_message)
        language = bot.detect_language(user_message)
        
        return jsonify({
            'response': response,
            'language': language.value,
            'bot_name': bot.name
        })
    
    except Exception as e:
        # Log the full error internally but return sanitized message to user
        app.logger.error(f"Error in chat endpoint: {str(e)}")
        return jsonify({
            'error': 'An error occurred while processing your message. Please try again.'
        }), 500


@app.route('/status/<complaint_id>', methods=['GET'])
def get_complaint_status(complaint_id):
    """
    Get complaint status directly
    
    Path parameter:
        complaint_id: Complaint ID (e.g., CG-2025-00045)
    
    Response:
    {
        "complaint_id": "CG-2025-00045",
        "status": "In Progress",
        ...
    }
    """
    try:
        if api_client:
            status_data = api_client.get_complaint_status(complaint_id)
            return jsonify(status_data)
        else:
            return jsonify({
                'error': 'API client not configured'
            }), 503
    
    except Exception as e:
        # Log the full error internally but return sanitized message to user
        app.logger.error(f"Error fetching complaint status for {complaint_id}: {str(e)}")
        return jsonify({
            'error': 'Unable to fetch complaint status. Please try again later.'
        }), 500


@app.route('/environment/<zone_id>', methods=['GET'])
def get_environmental_data(zone_id):
    """
    Get environmental data for a zone
    
    Path parameter:
        zone_id: Zone identifier
    
    Response:
    {
        "zone": "3",
        "aqi": 172,
        "pm25": 95.0,
        ...
    }
    """
    try:
        if api_client:
            env_data = api_client.get_environmental_data(zone_id)
            return jsonify(env_data)
        else:
            return jsonify({
                'error': 'API client not configured'
            }), 503
    
    except Exception as e:
        # Log the full error internally but return sanitized message to user
        app.logger.error(f"Error fetching environmental data for zone {zone_id}: {str(e)}")
        return jsonify({
            'error': 'Unable to fetch environmental data. Please try again later.'
        }), 500


@app.route('/performance', methods=['GET'])
def get_performance_rankings():
    """
    Get performance rankings
    
    Response:
    {
        "top_zones": [...],
        "recent_achievements": [...]
    }
    """
    try:
        if api_client:
            performance_data = api_client.get_performance_rankings()
            return jsonify(performance_data)
        else:
            return jsonify({
                'error': 'API client not configured'
            }), 503
    
    except Exception as e:
        # Log the full error internally but return sanitized message to user
        app.logger.error(f"Error fetching performance rankings: {str(e)}")
        return jsonify({
            'error': 'Unable to fetch performance rankings. Please try again later.'
        }), 500


@app.route('/', methods=['GET'])
def index():
    """Root endpoint with API information"""
    return jsonify({
        'service': 'City Guardian AI Assistant API',
        'version': '1.0.0',
        'endpoints': {
            '/health': 'GET - Health check',
            '/chat': 'POST - Send message to chatbot',
            '/status/<complaint_id>': 'GET - Get complaint status',
            '/environment/<zone_id>': 'GET - Get environmental data',
            '/performance': 'GET - Get performance rankings'
        },
        'documentation': 'See README.md for usage examples'
    })


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    print(f"Starting City Guardian AI Assistant on port {port}")
    print(f"Using {'Real' if api_key else 'Mock'} API Client")
    
    app.run(host='0.0.0.0', port=port, debug=debug)
