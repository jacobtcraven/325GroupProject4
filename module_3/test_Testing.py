class Testing:
    def test_scrape_object():
        obj = RawData.scrape("https://www.cnn.com/2024/04/16/sport/masters-no-phones-spt-intl/index.html")
        assert obj is not None
    
    def test_read_urls():
        urls = InputOutput.read_urls("urls.txt")
        assert urls is not None
        assert isinstance(urls, list)
        assert all(isinstance(url, str) for url in urls)