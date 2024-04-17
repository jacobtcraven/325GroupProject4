# Import needed classes and functions
from module_1.RawData import RawData, InputOutput
from module_2.FormatData import FormatData
from module_3.Testing import TestURLValidation, TestAccessibility, TestTitleExtraction, TestHTMLContentExtraction, Testing
from module_3.Testing import Testing, TestURLValidation, TestAccessibility, TestTitleExtraction, TestHTMLContentExtraction
import sys
import unittest

## Import openai and api key
import openai
from other.sk import sr_key


# Set the API key
openai.api_key = sr_key

class CustomPreCheckTests(unittest.TestCase):
    def test_file_exists(self):
        """Ensure the urls.txt file exists and is accessible."""
        self.assertTrue(Testing.test_url_text_exists(), "urls.txt file does not exist or is not accessible.")

    def test_urls_are_readable(self):
        """Check that urls.txt contains URLs and is readable."""
        self.assertTrue(Testing.test_read_urls(), "urls.txt cannot be read or does not contain valid URLs.")

    def test_scrape_functionality(self):
        """Ensure that the scrape function is operational before processing."""
        self.assertIsNotNone(Testing.test_scrape_object(), "Scrape function failed or returned None.")

    def test_title_type(self):
        """Test that the title extracted is a string."""
        self.assertIsInstance(Testing.test_title(), str, "The title obtained is not a string.")

def run_tests():
    # Create a test suite combining all test cases
    suite = unittest.TestSuite()

    # Adding unittest suites
    suite.addTest(unittest.makeSuite(TestURLValidation))
    suite.addTest(unittest.makeSuite(TestAccessibility))
    suite.addTest(unittest.makeSuite(TestTitleExtraction))
    suite.addTest(unittest.makeSuite(TestHTMLContentExtraction))
    suite.addTest(unittest.makeSuite(CustomPreCheckTests))  # Include custom tests

    # Run the tests
    runner = unittest.TextTestRunner()
    runner.run(suite)

def main():
    # Read the URLs from the file
    urls = InputOutput.read_urls('other/urls.txt')
    counter = 1

    for URL in urls:
        source = RawData.scrape(URL)
        InputOutput.write_to_file(str(source), f'Data/raw/raw{counter}.txt')
        title = FormatData.get_title(source)
        formatted = FormatData.remove_html(source)
        formatted = FormatData.add_newlines(formatted)
        InputOutput.write_to_file(formatted, f'Data/processed/formatted{counter}.txt')
        
        messages = [{"role": "system", "content": "You are an intelligent assistant."}]
        message = f"Make this article concise in under 50 words\n {formatted}"
        messages.append({"role": "user", "content": message})

        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content
        formatted_reply = FormatData.add_newlines(reply)
        summary = title + '\n' + formatted_reply
        InputOutput.write_to_file(summary, f'Data/summarized/summarized{counter}.txt')

        counter += 1

if __name__ == '__main__':
    if '--test' in sys.argv:
        run_tests()
    else:
        main()
