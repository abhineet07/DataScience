from bs4 import BeautifulSoup as soup, NavigableString, Tag
import requests

class Amazon:
    def __init__(self):
        self.url = ""

    def getPageSoup(self, url):
        self.url = url
        print(url)
        page = requests.get(url)
        page_html = page.text
        self.page_soup = soup(page_html, "html.parser")
        return self.page_soup

    def RewiewPage(self, page_soup):
        try:
            nextPageLink = page_soup.find('a', {'data-hook': 'see-all-reviews-link'})
            return "https://www.amazon.in" + nextPageLink['href']
        except:
            print("Failed at -> Amazon -> Rewiew page link")


# url = "https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B07KXBMYCW"
#
# amazon = Amazon()
# print(amazon.RewiewPage(amazon.getPageSoup(url)))

