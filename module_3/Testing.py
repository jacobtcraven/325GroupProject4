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