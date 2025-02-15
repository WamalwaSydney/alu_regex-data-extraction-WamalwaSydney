#!/usr/bin/env python3
import re

def extract_emails(text):
    pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    return re.findall(pattern, text)

def extract_urls(text):
    pattern = r'https?://(?:www\.)?[\w.-]+\.[a-zA-Z]{2,}(?:/\S*)?'
    return re.findall(pattern, text)

def extract_phone_numbers(text):
    pattern = r'(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}'
    return re.findall(pattern, text)

def extract_currency_amounts(text):
    pattern = r'\$(?:\d{1,3}(?:,\d{3})+|\d+)\.\d{2}'
    return re.findall(pattern, text)

# Example usage
if __name__ == "__main__":
    sample_text = """
    Contact us at user@example.com or support@company.co.uk.
    Visit https://www.example.com or https://sub.domain.org/path?query=param.
    Call (123) 456-7890, 123-456-7890, or 123.456.7890 today!
    Prices are $19.99 and $1,234.56.
    """

    print("Emails:", extract_emails(sample_text))
    print("URLs:", extract_urls(sample_text))
    print("Phone Numbers:", extract_phone_numbers(sample_text))
    print("Currency Amounts:", extract_currency_amounts(sample_text))
