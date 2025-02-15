# alu_regex-data-extraction-WamalwaSydney
Email Extraction: The regex \b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b ensures valid usernames and domains, including subdomains and TLDs.

URL Extraction: The regex https?://(?:www\.)?[\w.-]+\.[a-zA-Z]{2,}(?:/\S*)? matches URLs starting with http/https, optional www subdomain, and valid domain/path.

Phone Numbers: The regex (?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4} handles various separators and formats, ensuring 10-digit numbers.

Currency Amounts: The regex \$(?:\d{1,3}(?:,\d{3})+|\d+)\.\d{2} matches amounts with optional commas and mandatory two decimal places.
