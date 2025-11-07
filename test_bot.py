"""
Tests for City Guardian AI Assistant
"""

import unittest
from city_guardian_bot import CityGuardianBot, Intent, Language
from api_client import MockAPIClient


class TestCityGuardianBot(unittest.TestCase):
    """Test cases for City Guardian Bot"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.api_client = MockAPIClient()
        self.bot = CityGuardianBot(api_client=self.api_client)
    
    def test_language_detection_hindi(self):
        """Test Hindi language detection"""
        text = "मेरी शिकायत की स्थिति बताओ"
        language = self.bot.detect_language(text)
        self.assertEqual(language, Language.HINDI)
    
    def test_language_detection_english(self):
        """Test English language detection"""
        text = "What is my complaint status?"
        language = self.bot.detect_language(text)
        self.assertEqual(language, Language.ENGLISH)
    
    def test_intent_complaint_status(self):
        """Test complaint status intent detection"""
        text = "Complaint ID CG-2025-00045 ki status batao"
        intent = self.bot.detect_intent(text)
        self.assertEqual(intent, Intent.COMPLAINT_STATUS)
    
    def test_intent_environmental_data(self):
        """Test environmental data intent detection"""
        text = "Zone 3 ka AQI kaisa hai?"
        intent = self.bot.detect_intent(text)
        self.assertEqual(intent, Intent.ENVIRONMENTAL_DATA)
    
    def test_intent_complaint_registration(self):
        """Test complaint registration intent detection"""
        text = "Main nayi shikayat darj karna chahta hoon"
        intent = self.bot.detect_intent(text)
        self.assertEqual(intent, Intent.COMPLAINT_REGISTRATION)
    
    def test_intent_achievements(self):
        """Test achievements intent detection"""
        text = "Top performing zones kaun se hain?"
        intent = self.bot.detect_intent(text)
        self.assertEqual(intent, Intent.ACHIEVEMENTS)
    
    def test_extract_complaint_id(self):
        """Test complaint ID extraction"""
        text = "My complaint ID is CG-2025-00045"
        complaint_id = self.bot.extract_complaint_id(text)
        self.assertEqual(complaint_id, "CG-2025-00045")
    
    def test_extract_complaint_id_case_insensitive(self):
        """Test complaint ID extraction is case insensitive"""
        text = "complaint id cg-2025-12345"
        complaint_id = self.bot.extract_complaint_id(text)
        self.assertEqual(complaint_id, "CG-2025-12345")
    
    def test_extract_zone(self):
        """Test zone extraction"""
        text = "Zone 3 ka environmental data chahiye"
        zone = self.bot.extract_zone(text)
        self.assertEqual(zone, "3")
    
    def test_extract_zone_with_hyphen(self):
        """Test zone extraction with hyphen"""
        text = "Zone-5 ki information do"
        zone = self.bot.extract_zone(text)
        self.assertEqual(zone, "5")
    
    def test_complaint_registration_redirect_hindi(self):
        """Test complaint registration redirect in Hindi"""
        response = self.bot.handle_complaint_registration(Language.HINDI)
        self.assertIn("dedicated 'Complaint Registration' page", response)
        self.assertIn("support aur status update", response)
    
    def test_complaint_registration_redirect_english(self):
        """Test complaint registration redirect in English"""
        response = self.bot.handle_complaint_registration(Language.ENGLISH)
        self.assertIn("dedicated 'Complaint Registration' page", response)
        self.assertIn("support and status updates", response)
    
    def test_complaint_status_without_id(self):
        """Test complaint status request without ID"""
        text = "complaint status chahiye"
        response = self.bot.handle_complaint_status(text, Language.HINDI)
        self.assertIn("Complaint ID", response)
    
    def test_complaint_status_with_id(self):
        """Test complaint status request with ID"""
        text = "Status of CG-2025-00045"
        response = self.bot.handle_complaint_status(text, Language.ENGLISH)
        self.assertIn("CG-2025-00045", response)
        self.assertIn("In Progress", response)
    
    def test_environmental_data_without_zone(self):
        """Test environmental data request without zone"""
        text = "AQI kya hai?"
        response = self.bot.handle_environmental_data(text, Language.HINDI)
        self.assertIn("zone", response.lower())
    
    def test_environmental_data_with_zone(self):
        """Test environmental data request with zone"""
        text = "Zone 3 ka AQI batao"
        response = self.bot.handle_environmental_data(text, Language.HINDI)
        self.assertIn("Zone 3", response)
        self.assertIn("AQI", response)
    
    def test_process_message_greeting(self):
        """Test general greeting message"""
        response = self.bot.process_message("Hello")
        self.assertIn("City Guardian", response)
    
    def test_process_message_complaint_registration(self):
        """Test complaint registration attempt is redirected"""
        response = self.bot.process_message("I want to register a new complaint")
        self.assertIn("Complaint Registration", response)


class TestMockAPIClient(unittest.TestCase):
    """Test cases for Mock API Client"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.client = MockAPIClient()
    
    def test_get_complaint_status(self):
        """Test getting complaint status"""
        status = self.client.get_complaint_status("CG-2025-00045")
        self.assertEqual(status['complaint_id'], "CG-2025-00045")
        self.assertIn('status', status)
        self.assertIn('zone', status)
    
    def test_get_environmental_data(self):
        """Test getting environmental data"""
        data = self.client.get_environmental_data("3")
        self.assertEqual(data['zone'], "3")
        self.assertIn('aqi', data)
        self.assertIn('pm25', data)
    
    def test_get_performance_rankings(self):
        """Test getting performance rankings"""
        data = self.client.get_performance_rankings()
        self.assertIn('top_zones', data)
        self.assertIn('recent_achievements', data)
        self.assertTrue(len(data['top_zones']) > 0)


if __name__ == '__main__':
    unittest.main()
