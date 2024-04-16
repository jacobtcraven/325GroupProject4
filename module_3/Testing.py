import unittest
import requests
from module_1.RawData import RawData, InputOutput
from module_2.FormatData import FormatData

class TestValidation(unittest.TestCase):
    def test_url_contains_http(self):
        """Test that URLs contain 'http://' or 'https://'."""
        urls = InputOutput.read_urls('/Users/alyabouzaid/Desktop/325GroupProject4/other/urls.txt')
        self.assertTrue(all('http://' in url or 'https://' in url for url in urls), "URLs must start with 'http://' or 'https://'")

    def test_url_accessibility(self):
        """Test that URLs are accessible and return a successful HTTP status code."""
        urls = InputOutput.read_urls('/Users/alyabouzaid/Desktop/325GroupProject4/other/urls.txt')
        for url in urls:
            with self.subTest(url=url):
                response = requests.get(url, timeout=10)
                self.assertEqual(response.status_code, 200, f"URL {url} did not return a 200 OK status code.")

    def test_title_received(self):
        """Test that a title is received from the HTML content."""
        urls = InputOutput.read_urls('/Users/alyabouzaid/Desktop/325GroupProject4/other/urls.txt')
        for url in urls:
            with self.subTest(url=url):
                html_data = RawData.scrape(url)
                title = FormatData.get_title(html_data)
                self.assertIsNotNone(title, f"No title found for URL {url}")
                self.assertNotEqual(title.strip(), '', f"Title is empty for URL {url}")

    def test_html_content_extraction(self):
        """Test that HTML content extraction works correctly."""
        urls = InputOutput.read_urls('/Users/alyabouzaid/Desktop/325GroupProject4/other/urls.txt')
        for url in urls:
            with self.subTest(url=url):
                html_data = RawData.scrape(url)
                content = FormatData.remove_html(html_data)
                # Check if the content is not None and not empty
                self.assertIsNotNone(content, f"No content was extracted for URL {url}")
                self.assertNotEqual(content.strip(), '', f"Extracted content is empty for URL {url}")
                # Optionally check for a known piece of content
                # self.assertIn('specific text known to be part of the page', content, f"Expected content not found in HTML for URL {url}")
