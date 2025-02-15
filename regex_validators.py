import re

# 1. Email Address Validation
def validate_email(email):
    """Validates email using regex pattern."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# 2. URL Validation
def validate_url(url):
    """Validates URL using regex pattern."""
    pattern = r'^https?:\/\/(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\/[a-zA-Z0-9#?&%=_.-]+)*$'
    return re.match(pattern, url) is not None

# 3. Phone Number Validation
def validate_phone(phone):
    """Validates phone number using regex pattern."""
    pattern = r'^(?:\(\d{3}\)\s?|\d{3}[-.\s]?)\d{3}[-.\s]?\d{4}$'
    return re.match(pattern, phone) is not None

# 4. Credit Card Number Validation
def validate_credit_card(card):
    """Validates credit card number using regex pattern."""
    pattern = r'^(?:\d{4}[-\s]?){3}\d{4}$'
    return re.match(pattern, card) is not None

# 5. Time Validation (12-hour & 24-hour format)
def validate_time(time_str):
    """Validates time (12-hour & 24-hour formats) using regex pattern."""
    pattern = r'^(?:[01]?\d|2[0-3]):([0-5]\d)(?:\s?[APap][Mm])?$'
    return re.match(pattern, time_str) is not None

# 6. HTML Tag Extraction
def extract_html_tags(text):
    """Extracts HTML tags from a given string."""
    pattern = r'<([a-zA-Z][a-zA-Z0-9]*)\b[^>]*>(.*?)</\1>'
    return re.findall(pattern, text)

# 7. Hashtag Validation
def validate_hashtag(hashtag):
    """Validates hashtag using regex pattern."""
    pattern = r'^#[a-zA-Z0-9]+$'
    return re.match(pattern, hashtag) is not None

# 8. Currency Amount Validation
def validate_currency(currency):
    """Validates currency amount using regex pattern."""
    pattern = r'^\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?$'
    return re.match(pattern, currency) is not None