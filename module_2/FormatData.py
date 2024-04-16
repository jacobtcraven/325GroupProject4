'''This module contains the FormatData class which contains methods to format provided html data'''

'''Single Responsibility Principle'''

from bs4 import BeautifulSoup


class FormatData:
    def get_title(raw):
        text = raw.find("title")
        return text.get_text()

    ## Removes the html tags from the raw data
    def remove_html(raw):
        text = raw.find("div", class_='caas-body')
        return text.get_text()
    
    ## Add a new line for every 20 words in the article
    def add_newlines(article):
        article = article.split()
        for i in range(len(article)):
            if i % 20 == 0:
                article.insert(i, '\n')
        return ' '.join(article)