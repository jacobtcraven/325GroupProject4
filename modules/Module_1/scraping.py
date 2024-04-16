# scraping.py

"""
This module is responsible for fetching HTML content from a given URL and optionally saving it as raw HTML.
It demonstrates the Single Responsibility Principle (SRP) by focusing solely on web scraping functionalities.

Single Responsibility Principle (SRP) is applied
This makes the system more maintainable and adaptable to change.

Functions:
    fetch_html(url, save_raw=True): Fetches the HTML content from the specified URL. It can also save the raw HTML to a file.
    save_raw_html(html_content, url): Saves the raw HTML content to a specified file within the Data/raw directory.

The SRP enhances maintainability and scalability by isolating the web scraping logic, making the module easy to update or replace if necessary.
"""

import os
import requests
from urllib.parse import urlparse, quote

def fetch_html(url, save_raw=True):
    """Fetches the HTML content of a given URL and optionally saves it to a file.

    Args:
        url (str): The URL of the webpage to scrape.
        save_raw (bool): Whether to save the raw HTML content to a file.

    Returns:
        str: Raw HTML content of the webpage.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  
        html_content = response.text

        if save_raw:
            save_raw_html(html_content, url)

        return html_content
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def save_raw_html(html_content, url):
    """Saves the raw HTML content to a file in the Data/raw directory.

    Args:
        html_content (str): The HTML content to save.
        url (str): The URL of the webpage, used to generate the filename.
    """
    filename = quote(url, safe='')[7:200]  
    filename += "_raw.txt"
    raw_path = os.path.join('Data', 'raw', filename)

    os.makedirs(os.path.dirname(raw_path), exist_ok=True)

    with open(raw_path, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"Saved raw HTML content to {raw_path}")
