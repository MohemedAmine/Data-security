import re
from urllib.parse import urlparse
import numpy as np
import pandas as pd
from tld import get_tld
import joblib

# Load the scaler
scaler = joblib.load("scaler.pkl")

# Extract domain from URL
def process_tld(url):
    try:
        res = get_tld(url, as_object=True, fail_silently=False, fix_protocol=True)
        return res.parsed_url.netloc
    except:
        return None

# Detect abnormal URL (hostname not in the full URL)
def abnormal_url(url: str) -> int:
    hostname = str(urlparse(url).hostname)
    return 0 if re.search(hostname, url) is None else 1

# Check if HTTPS is used
def http_secured(url: str) -> int:
    return 1 if urlparse(url).scheme == 'https' else 0

# Count digits in URL
def digit_count(url: str) -> int:
    return sum(c.isdigit() for c in url)

# Count letters in URL
def letter_count(url: str) -> int:
    return sum(c.isalpha() for c in url)

# Detect usage of URL shortening services
def shortening_service(url: str) -> int:
    pattern = (
        r'bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
        r'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
        r'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
        r'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|lnkd\.in|'
        r'db\.tt|qr\.ae|adf\.ly|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|ity\.im|'
        r'q\.gs|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
        r'prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|'
        r'tr\.im|link\.zip\.net'
    )
    return 1 if re.search(pattern, url) else 0

# Detect if URL contains an IP address
def has_ip_address(url: str) -> int:
    pattern = (r'(([01]?\d\d?|2[0-4]\d|25[0-5])\.){3}'
               r'([01]?\d\d?|2[0-4]\d|25[0-5])')
    return 1 if re.search(pattern, url) else 0

# Main feature extraction function
def extract_features(df: pd.DataFrame) -> pd.DataFrame:
    df['url'] = df['url'].replace('www', '', regex=True)
    df['url_length'] = df['url'].apply(len)

    # Uncomment if domain processing is needed
    # df['domain'] = df['url'].apply(process_tld)

    # Special characters to count
    special_chars = ['@', '?', '-', '=', '.', '#', '%', '+', '$', '!', '*', ',', '//']
    for char in special_chars:
        df[char] = df['url'].apply(lambda x: x.count(char))

    # Additional features
    df['abnormal_url'] = df['url'].apply(abnormal_url)
    df['https'] = df['url'].apply(http_secured)
    df['digits'] = df['url'].apply(digit_count)
    df['letters'] = df['url'].apply(letter_count)
    df['shortening_service'] = df['url'].apply(shortening_service)
    df['has_ip_address'] = df['url'].apply(has_ip_address)

    return df

# Final preprocessing: normalization using the scaler
def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    feature_cols = ['url_length', '@', '?', '-', '=', '.', '#', '%', '+', '$', '!', '*',
                    ',', '//', 'abnormal_url', 'https', 'digits', 'letters',
                    'shortening_service', 'has_ip_address']
    df[feature_cols] = scaler.transform(df[feature_cols])
    return df[feature_cols]
