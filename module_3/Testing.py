## Import needed classes and functions
from module_1.RawData import RawData, InputOutput
from module_2.FormatData import FormatData

class Testing:
    def test_scrape_object():
        obj = RawData.scrape("https://www.cnn.com/2024/04/16/sport/masters-no-phones-spt-intl/index.html")
        assert obj != None
    
    def test_read_urls():
        urls = InputOutput.read_urls("urls.txt")
        assert urls != None
        assert isinstance(urls, list)
        for url in urls:
            assert isinstance(url, str)

    def test_title():
        obj = RawData.scrape("https://www.cnn.com/2024/04/16/sport/masters-no-phones-spt-intl/index.html")
        title = FormatData.title(obj)
        assert title != None
        assert isinstance(title, str)
    
    def test_url_text_exists():
        assert os.path.exists("other/urls.txt") == True

class TestURLValidation(unittest.TestCase):
    def test_url_contains_http(self):
        """Test that URLs contain 'http://' or 'https://'."""
        urls = InputOutput.read_urls('/Users/alyabouzaid/Desktop/325GroupProject4/other/urls.txt')
        self.assertTrue(all('http://' in url or 'https://' in url for url in urls), "URLs must start with 'http://' or 'https://'")

class TestAccessibility(unittest.TestCase):
    def test_url_accessibility(self):
        """Test that URLs are accessible and return a successful HTTP status code."""
        urls = InputOutput.read_urls('/Users/alyabouzaid/Desktop/325GroupProject4/other/urls.txt')
        for url in urls:
            with self.subTest(url=url):
                response = requests.get(url, timeout=10)
                self.assertEqual(response.status_code, 200, f"URL {url} did not return a 200 OK status code.")

class TestTitleExtraction(unittest.TestCase):
    def test_title_received(self):
        """Test that a title is received from the HTML content."""
        urls = InputOutput.read_urls('/Users/alyabouzaid/Desktop/325GroupProject4/other/urls.txt')
        for url in urls:
            with self.subTest(url=url):
                html_data = RawData.scrape(url)
                title = FormatData.get_title(html_data)
                self.assertIsNotNone(title, f"No title found for URL {url}")
                self.assertNotEqual(title.strip(), '', f"Title is empty for URL {url}")

class TestHTMLContentExtraction(unittest.TestCase):
    def test_html_content_extraction(self):
        """Test that HTML content extraction works correctly."""
        urls = InputOutput.read_urls('/Users/alyabouzaid/Desktop/325GroupProject4/other/urls.txt')
        for url in urls:
            with self.subTest(url=url):
                html_data = RawData.scrape(url)
                content = FormatData.remove_html(html_data)
                self.assertIsNotNone(content, f"No content was extracted for URL {url}")
                self.assertNotEqual(content.strip(), '', f"Extracted content is empty for URL {url}")

if __name__ == '__main__':
    unittest.main()
