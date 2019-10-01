from googlesearch import search
from GoogleToAmazon2 import *

# query = "samsung a50 amazon"
class Google:
    def __init__(self):
        self.query = ""
        self.resultsNum = 1

    def search(self, query):
        self.query = query
        # results = search(self.query, tld="co.in", num=10, stop=3, pause=4)

        self.results = []
        for res in search(self.query, tld="co.in", num=1, stop=1, pause=5):
            self.results.append(str(res))

        return self.results

    def searchn(self, query, resultsNum):
        self.query = query
        # self.resultsNum = resultsNum
        # results = search(self.query, tld="co.in", num=10, stop=3, pause=4)

        self.results = []
        for res in search(self.query, tld="co.in", num=resultsNum, stop=resultsNum, pause=3):
            # print("GOOGLE : ", res)
            self.results.append(str(res))

        return self.results


# for j in search(query, tld="co.in", num=10, stop=3, pause=4):
#     print(j)
#     print(type(j))


# google = Google()
# amazon = Amazon()
# res = google.searchn("samsung a70 product-reviews amazon india", 5)
# print(res)
# print("res[0] = ", res[0])
# print("amzon: ", amazon.RewiewPage(amazon.getPageSoup(res[0])))
#
# for r in res:
#     # print(amazon.RewiewPage(amazon.getPageSoup(r)))
#     print(r)
#     break