import requests
from bs4 import BeautifulSoup as soup, NavigableString, Tag
from GoogleToAmazon import *
import re

class Gadgets:
    def __init__(self, query):
        google = Google()
        URLS = google.searchn(query, 10)
        # print(*URLS, sep='\n')

        exp = re.compile('user-reviews')
        url = ""
        for link in URLS:
            link = str(link)
            if re.search(exp, link):
                url = link
                break

        page_soup = self.getPageSoup(url)
        self.analysis(page_soup)

    def getPageSoup(self, url):
        page = requests.get(url, verify=False)
        page_html = page.text
        page_soup = soup(page_html, "html.parser")
        return page_soup

    def analysis(self, page_soup):
        # TITLE
        titles_list = []
        title = page_soup.findAll("div", {"class": "_flx _cmttl"})
        for t in title:
            titles_list.append(str(t.text).strip())

        # COMMENTS
        comments_list = []
        comments = page_soup.findAll("div", {"class": "_cmttxt"})
        for cmt in comments:
            comments_list.append(str(cmt.text).strip())

        main_box = page_soup.findAll("ul", {"class": "_pdcmnt rnr_cnt"})
        new_soup = soup(str(main_box), 'html.parser')

        # STARS
        stars_list = []
        stars = new_soup.findAll("span", {"class": "selected"})
        for star in stars:
            point = int(re.findall(r'\d+',star["style"])[0]) // 20
            stars_list.append(point)



# gd = gadgets360("samsung s10 gadgets 360 user-reviews")
gdt = Gadgets("samsung a50 gadgets 360 user-reviews")