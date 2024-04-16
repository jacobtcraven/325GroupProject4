# processing.py

"""
This module processes HTML content, extracting relevant information such as the article's title, content, and author.
It adheres to the Single Responsibility Principle (SRP) by focusing on the parsing and data extraction tasks.

Single Responsibility Principle (SRP) is applied
This makes the system more maintainable and adaptable to change.

Functions:
    parse_article(html_content): Parses the given HTML content and extracts the article's title, content, and author.

By following the SRP, this module can evolve independently of the rest of the system, ensuring changes in processing logic do not affect other components.
"""

from bs4 import BeautifulSoup

def parse_article(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    title = soup.find('h1').get_text(strip=True)
    
    content = ''
    for paragraph in soup.find_all('p'):
        content += paragraph.get_text(strip=True) + '\n'
    
    author_elem = soup.find('div', class_='headline__sub-text').find('span')
    author = author_elem.get_text().strip() if author_elem else "Author not found"


    return {
        'title': title,
        'content': content.strip(),
        'author': author,
    }
