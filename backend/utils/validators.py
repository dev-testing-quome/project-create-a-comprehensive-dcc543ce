# Validation utilities for {project_name}
from typing import Any, Dict, List
import re

def validate_email(email: str) -> bool:
    '''Validate email format'''
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone: str) -> bool:
    '''Validate phone number format'''
    pattern = r'^\+?1?\d{9,15}$'
    return re.match(pattern, phone) is not None

def sanitize_input(text: str) -> str:
    '''Basic input sanitization'''
    return text.strip()[:1000]  # Limit length and strip whitespace 