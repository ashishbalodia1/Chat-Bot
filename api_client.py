"""
API Client for City Guardian Bot
Handles all external API calls to municipal services
"""

import requests
from typing import Dict, Optional
from dataclasses import dataclass


@dataclass
class ComplaintStatus:
    """Complaint status data structure"""
    complaint_id: str
    status: str
    zone: str
    team: str
    estimated_days: int
    details: str


@dataclass
class EnvironmentalData:
    """Environmental data structure"""
    zone: str
    aqi: int
    pm25: float
    humidity: float
    wind_speed: float
    noise_level: Optional[float] = None
    water_quality: Optional[str] = None


@dataclass
class PerformanceData:
    """Performance/ranking data structure"""
    top_zones: list
    achievements: list


class MunicipalAPIClient:
    """
    Client for interacting with Raipur Municipal Corporation APIs
    
    API Endpoints:
    - GET /complaint/status?id=[ID]
    - GET /environment/data?zone=[ZoneID]
    - GET /performance/rankings
    """
    
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        """
        Initialize API client
        
        Args:
            base_url: Base URL for the municipal API
            api_key: Optional API key for authentication
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.session = requests.Session()
        
        if api_key:
            self.session.headers.update({
                'Authorization': f'Bearer {api_key}'
            })
    
    def get_complaint_status(self, complaint_id: str) -> Dict:
        """
        Get complaint status from API
        
        Args:
            complaint_id: Complaint ID (format: CG-YYYY-NNNNN)
            
        Returns:
            Dict containing complaint status information
            
        Raises:
            requests.RequestException: If API call fails
        """
        endpoint = f"{self.base_url}/complaint/status"
        params = {'id': complaint_id}
        
        try:
            response = self.session.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch complaint status: {str(e)}")
    
    def get_environmental_data(self, zone_id: str) -> Dict:
        """
        Get environmental data for a zone
        
        Args:
            zone_id: Zone identifier
            
        Returns:
            Dict containing environmental data
            
        Raises:
            requests.RequestException: If API call fails
        """
        endpoint = f"{self.base_url}/environment/data"
        params = {'zone': zone_id}
        
        try:
            response = self.session.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch environmental data: {str(e)}")
    
    def get_performance_rankings(self) -> Dict:
        """
        Get performance rankings and achievements
        
        Returns:
            Dict containing performance and ranking data
            
        Raises:
            requests.RequestException: If API call fails
        """
        endpoint = f"{self.base_url}/performance/rankings"
        
        try:
            response = self.session.get(endpoint, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch performance rankings: {str(e)}")


class MockAPIClient:
    """
    Mock API client for testing without actual API connection
    """
    
    def get_complaint_status(self, complaint_id: str) -> Dict:
        """Mock complaint status response"""
        return {
            'complaint_id': complaint_id,
            'status': 'In Progress',
            'status_code': 'IN_PROGRESS',
            'zone': '4',
            'team': 'Sewage Unit',
            'estimated_resolution_days': 3,
            'details': 'Team has been assigned and work is in progress',
            'created_at': '2025-11-01T10:00:00Z',
            'last_updated': '2025-11-05T14:30:00Z'
        }
    
    def get_environmental_data(self, zone_id: str) -> Dict:
        """Mock environmental data response"""
        return {
            'zone': zone_id,
            'aqi': 172,
            'aqi_category': 'Unhealthy',
            'pm25': 95.0,
            'pm25_target': 40.0,
            'humidity': 65.0,
            'wind_speed': 12.5,
            'wind_direction': 'NE',
            'noise_level': 75.0,
            'temperature': 28.5,
            'advisory': 'Avoid outdoor exercise; masks recommended for vulnerable people',
            'measured_at': '2025-11-07T10:00:00Z'
        }
    
    def get_performance_rankings(self) -> Dict:
        """Mock performance rankings response"""
        return {
            'top_zones': [
                {
                    'zone': '2',
                    'rank': 1,
                    'metric': 'PM2.5 Improvement',
                    'value': '15%',
                    'score': 95
                },
                {
                    'zone': '5',
                    'rank': 2,
                    'metric': 'Complaint Resolution',
                    'value': '95%',
                    'score': 92
                }
            ],
            'recent_achievements': [
                'Zone 2 reduced PM2.5 levels by 15% in last quarter',
                'Zone 5 achieved 95% complaint resolution rate',
                'Zone 1 completed 100% garbage collection efficiency'
            ],
            'generated_at': '2025-11-07T10:00:00Z'
        }
