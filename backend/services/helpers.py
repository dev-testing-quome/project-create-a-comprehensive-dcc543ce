# Helper services for project-create-a-comprehensive
from typing import Dict, Any, List, Optional
import logging

logger = logging.getLogger(__name__)

class EcommerceHelpers:
    '''Helper utilities for ecommerce applications'''
    
    @staticmethod
    def validate_input(data: Dict[str, Any]) -> bool:
        '''Validate input data'''
        return isinstance(data, dict) and len(data) > 0
    
    @staticmethod
    def format_response(data: Any) -> Dict[str, Any]:
        '''Format API response'''
        return {"success": True, "data": data}
    
    @staticmethod
    def handle_error(error: Exception) -> Dict[str, Any]:
        '''Handle and format errors'''
        logger.error(f"Error occurred: {error}")
        return {"success": False, "error": str(error)} 