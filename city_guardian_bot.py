"""
City Guardian AI Assistant
AI chatbot for Raipur Municipal Corporation support interface
"""

import re
import json
from typing import Dict, Optional, Tuple
from enum import Enum


class Intent(Enum):
    """User intent types"""
    COMPLAINT_STATUS = "complaint_status"
    ENVIRONMENTAL_DATA = "environmental_data"
    POLICY_INFO = "policy_info"
    ACHIEVEMENTS = "achievements"
    COMPLAINT_REGISTRATION = "complaint_registration"
    UNKNOWN = "unknown"


class Language(Enum):
    """Supported languages"""
    HINDI = "hi"
    ENGLISH = "en"


class CityGuardianBot:
    """
    City Guardian AI Assistant for Raipur Municipal Corporation
    
    Features:
    - Complaint status tracking
    - Environmental data summaries
    - Policy and scheme information
    - Zone achievements and milestones
    - Bilingual support (Hindi & English)
    """
    
    def __init__(self, api_client=None):
        """
        Initialize City Guardian Bot
        
        Args:
            api_client: Optional API client for external data fetching
        """
        self.api_client = api_client
        self.name = "City Guardian"
        
        # Complaint registration redirect message
        self.redirect_messages = {
            Language.HINDI: "Aapki shikayat darj karne ke liye, kripya dedicated 'Complaint Registration' page ka upyog karen. Main yahan support aur status update ke liye hoon.",
            Language.ENGLISH: "To register your complaint, please use the dedicated 'Complaint Registration' page. I am here for support and status updates."
        }
        
    def detect_language(self, text: str) -> Language:
        """
        Detect language from user input
        
        Args:
            text: User input text
            
        Returns:
            Detected language (Hindi or English)
        """
        # Simple detection: check for Hindi Unicode characters
        hindi_pattern = re.compile(r'[\u0900-\u097F]')
        if hindi_pattern.search(text):
            return Language.HINDI
        return Language.ENGLISH
    
    def detect_intent(self, text: str) -> Intent:
        """
        Detect user intent from input text
        
        Args:
            text: User input text
            
        Returns:
            Detected intent
        """
        text_lower = text.lower()
        
        # Complaint registration keywords (check first to prevent misclassification)
        registration_keywords = [
            'register complaint', 'new complaint', 'file complaint',
            'shikayat darj', 'nayi shikayat', 'complaint karna',
            'complain karna', 'register karo', 'darj karo'
        ]
        if any(keyword in text_lower for keyword in registration_keywords):
            return Intent.COMPLAINT_REGISTRATION
        
        # Complaint status keywords
        status_keywords = [
            'status', 'track', 'complaint id', 'reference number',
            'shikayat ka status', 'complaint ki sthiti', 'cg-'
        ]
        if any(keyword in text_lower for keyword in status_keywords):
            return Intent.COMPLAINT_STATUS
        
        # Achievements keywords (check before policy to avoid confusion)
        achievement_keywords = [
            'achievement', 'milestone', 'ranking', 'performance',
            'uplabdhi', 'pragati', 'top zone', 'best zone', 'achhe zones',
            'performing zones', 'sabse achhe'
        ]
        if any(keyword in text_lower for keyword in achievement_keywords):
            return Intent.ACHIEVEMENTS
        
        # Environmental data keywords
        env_keywords = [
            'aqi', 'air quality', 'pollution', 'pm2.5', 'environment',
            'vayu gunvatta', 'pradushan', 'paryavaran', 'humidity',
            'wind', 'noise', 'water quality'
        ]
        if any(keyword in text_lower for keyword in env_keywords):
            return Intent.ENVIRONMENTAL_DATA
        
        # Policy keywords
        policy_keywords = [
            'policy', 'scheme', 'process', 'procedure', 'how to',
            'niti', 'yojana', 'prakriya', 'kaise', 'documents',
            'form', 'apply'
        ]
        if any(keyword in text_lower for keyword in policy_keywords):
            return Intent.POLICY_INFO
        
        return Intent.UNKNOWN
    
    def extract_complaint_id(self, text: str) -> Optional[str]:
        """
        Extract complaint ID from text
        
        Args:
            text: User input text
            
        Returns:
            Complaint ID if found, None otherwise
        """
        # Pattern: CG-YYYY-NNNNN
        pattern = r'CG-\d{4}-\d{5}'
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(0).upper()
        return None
    
    def extract_zone(self, text: str) -> Optional[str]:
        """
        Extract zone information from text
        
        Args:
            text: User input text
            
        Returns:
            Zone ID if found, None otherwise
        """
        # Pattern: Zone N or Zone-N
        pattern = r'zone[-\s]*(\d+)'
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1)
        return None
    
    def handle_complaint_status(self, text: str, language: Language) -> str:
        """
        Handle complaint status inquiry
        
        Args:
            text: User input text
            language: Detected language
            
        Returns:
            Response message
        """
        complaint_id = self.extract_complaint_id(text)
        
        if not complaint_id:
            if language == Language.HINDI:
                return "Kripya apni Complaint ID provide karen (format: CG-2025-00001)."
            return "Please provide your Complaint ID (format: CG-2025-00001)."
        
        # Call API if client is available
        if self.api_client:
            try:
                status_data = self.api_client.get_complaint_status(complaint_id)
                return self._format_complaint_status(status_data, language)
            except Exception as e:
                if language == Language.HINDI:
                    return f"Complaint status lene mein samasya: {str(e)}"
                return f"Error fetching complaint status: {str(e)}"
        
        # Mock response for demonstration
        if language == Language.HINDI:
            return f"Complaint {complaint_id}: Team Assigned (Zone 4 - Sewage Unit). Status: In Progress. Expected resolution: 3 days."
        return f"Complaint {complaint_id}: Team Assigned (Zone 4 - Sewage Unit). Current status: In Progress. Expected resolution: 3 days."
    
    def handle_environmental_data(self, text: str, language: Language) -> str:
        """
        Handle environmental data inquiry
        
        Args:
            text: User input text
            language: Detected language
            
        Returns:
            Response message
        """
        zone = self.extract_zone(text)
        
        if not zone:
            if language == Language.HINDI:
                return "Kripya zone number batayein (jaise: Zone 1, Zone 2)."
            return "Please specify the zone number (e.g., Zone 1, Zone 2)."
        
        # Call API if client is available
        if self.api_client:
            try:
                env_data = self.api_client.get_environmental_data(zone)
                return self._format_environmental_data(env_data, language)
            except Exception as e:
                if language == Language.HINDI:
                    return f"Environmental data lene mein samasya: {str(e)}"
                return f"Error fetching environmental data: {str(e)}"
        
        # Mock response for demonstration
        if language == Language.HINDI:
            return f"Zone {zone} — AQI: 172 (Unhealthy). PM2.5: 95 µg/m³ — target < 40 µg/m³. Advisory: Bahar exercise se bachen; vulnerable logo ke liye mask ki sifaarish."
        return f"Zone {zone} — AQI: 172 (Unhealthy). PM2.5: 95 µg/m³ — target < 40 µg/m³. Advisory: Avoid outdoor exercise; masks recommended for vulnerable people."
    
    def handle_policy_info(self, text: str, language: Language) -> str:
        """
        Handle policy and scheme information inquiry
        
        Args:
            text: User input text
            language: Detected language
            
        Returns:
            Response message
        """
        # This would typically query a knowledge base
        if language == Language.HINDI:
            return "Municipal policies aur schemes ki jaankari ke liye, kripya specific yojana ka naam batayein ya municipal office se sampark karen. Office hours: 10 AM - 5 PM."
        return "For information on municipal policies and schemes, please specify the scheme name or contact the municipal office. Office hours: 10 AM - 5 PM."
    
    def handle_achievements(self, text: str, language: Language) -> str:
        """
        Handle zone achievements inquiry
        
        Args:
            text: User input text
            language: Detected language
            
        Returns:
            Response message
        """
        # Call API if client is available
        if self.api_client:
            try:
                performance_data = self.api_client.get_performance_rankings()
                return self._format_achievements(performance_data, language)
            except Exception as e:
                if language == Language.HINDI:
                    return f"Achievement data lene mein samasya: {str(e)}"
                return f"Error fetching achievement data: {str(e)}"
        
        # Mock response for demonstration
        if language == Language.HINDI:
            return "Top Zones: Zone 2 (PM2.5 mein 15% sudhar), Zone 5 (complaint resolution mein 95% success). Badhai ho!"
        return "Top Zones: Zone 2 (15% improvement in PM2.5), Zone 5 (95% success in complaint resolution). Congratulations!"
    
    def handle_complaint_registration(self, language: Language) -> str:
        """
        Handle complaint registration attempt (redirect to proper page)
        
        Args:
            language: Detected language
            
        Returns:
            Redirect message
        """
        return self.redirect_messages[language]
    
    def _format_complaint_status(self, data: Dict, language: Language) -> str:
        """Format complaint status data for response"""
        complaint_id = data.get('complaint_id', 'N/A')
        status = data.get('status', 'Unknown')
        zone = data.get('zone', 'N/A')
        team = data.get('team', 'N/A')
        days = data.get('estimated_resolution_days', 'N/A')
        
        if language == Language.HINDI:
            return f"Complaint {complaint_id}: Team Assigned (Zone {zone} - {team}). Status: {status}. Expected resolution: {days} days."
        return f"Complaint {complaint_id}: Team Assigned (Zone {zone} - {team}). Current status: {status}. Expected resolution: {days} days."
    
    def _format_environmental_data(self, data: Dict, language: Language) -> str:
        """Format environmental data for response"""
        zone = data.get('zone', 'N/A')
        aqi = data.get('aqi', 'N/A')
        aqi_category = data.get('aqi_category', 'Unknown')
        pm25 = data.get('pm25', 0)
        pm25_target = data.get('pm25_target', 40)
        advisory = data.get('advisory', '')
        
        if language == Language.HINDI:
            return f"Zone {zone} — AQI: {aqi} ({aqi_category}). PM2.5: {pm25} µg/m³ — target < {pm25_target} µg/m³. Advisory: {advisory if advisory else 'Koi vishesh salaah nahi'}"
        return f"Zone {zone} — AQI: {aqi} ({aqi_category}). PM2.5: {pm25} µg/m³ — target < {pm25_target} µg/m³. Advisory: {advisory if advisory else 'No specific advisory'}"
    
    def _format_achievements(self, data: Dict, language: Language) -> str:
        """Format achievements data for response"""
        top_zones = data.get('top_zones', [])
        achievements = data.get('recent_achievements', [])
        
        zone_text = ", ".join([f"Zone {z['zone']} ({z['value']} {z['metric']})" for z in top_zones[:2]])
        
        if language == Language.HINDI:
            return f"Top Zones: {zone_text}. Badhai ho!"
        return f"Top Zones: {zone_text}. Congratulations!"
    
    def process_message(self, user_input: str) -> str:
        """
        Process user message and generate response
        
        Args:
            user_input: User's input message
            
        Returns:
            Bot's response message
        """
        # Detect language
        language = self.detect_language(user_input)
        
        # Detect intent
        intent = self.detect_intent(user_input)
        
        # Route to appropriate handler
        if intent == Intent.COMPLAINT_REGISTRATION:
            return self.handle_complaint_registration(language)
        elif intent == Intent.COMPLAINT_STATUS:
            return self.handle_complaint_status(user_input, language)
        elif intent == Intent.ENVIRONMENTAL_DATA:
            return self.handle_environmental_data(user_input, language)
        elif intent == Intent.POLICY_INFO:
            return self.handle_policy_info(user_input, language)
        elif intent == Intent.ACHIEVEMENTS:
            return self.handle_achievements(user_input, language)
        else:
            if language == Language.HINDI:
                return "Namaste! Main City Guardian hoon. Main aapki madad kar sakta hoon: Complaint status, Environmental data, Policies, ya Achievements ke baare mein."
            return "Hello! I am City Guardian. I can help you with: Complaint status, Environmental data, Policies, or Achievements."


def main():
    """Main function for testing the bot"""
    bot = CityGuardianBot()
    
    print("City Guardian AI Assistant")
    print("=" * 50)
    print("Type 'quit' to exit\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Thank you for using City Guardian!")
            break
        
        response = bot.process_message(user_input)
        print(f"Bot: {response}\n")


if __name__ == "__main__":
    main()
