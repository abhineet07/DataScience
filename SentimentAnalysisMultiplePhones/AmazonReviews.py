import requests
from GoogleToAmazon import *
from GoogleToAmazon2 import *
from bs4 import BeautifulSoup as soup, NavigableString, Tag
from textblob import TextBlob
import re
from Trie import *
from ExcelWriter import *

class Node():
    def __init__(self, data, index, word_index, inCommentIndex, polarity):
        self.data = data
        self.index = index
        self.word_index = word_index
        self.polarity = polarity
        self.inCommentIndex = inCommentIndex
        self.visited = False
        self.neighbourIndex = -1
        self.sentiment = 'Neutral'

    def __repr__(self):
        return str(self.data) + "->" + str(self.index) + " (" + str(self.word_index) + ")" + " (" + str(self.inCommentIndex) + ")"

    def getData(self):
        return self.data

    def getIndex(self):
        return self.index

    def getDistance(self):
        return self.distance

    def getNeighbourIndex(self):
        return self.neighbourIndex

    def setNeighbourIndex(self, i):
        self.neighbourIndex = i

    def setSentiment(self, sentiment):
        self.sentiment = sentiment

class AmazonUtil:
    def __init__(self, query, pages):
        self.query = query
        self.pages = int(pages)

        self.positives = ["good", "great", "decent", "amazing", "excellent", "sexy", "superb", "fast", "awesome",
                          "nice",
                          "best", "better",
                          "perfect", "perfection", "beast", "great", "fantastic", "faster", " fabulous", "blazing",
                          "love",
                          "marvellous",
                          "charge", "smooth", "beautifully", "beautiful", "superb"]
        self.negatives = ["very bad", "bad", "disappiontment", "wrong", "never", "slow", "no", "not good", "not work",
                          "not",
                          "heat",
                          "issue", "defect", "slowest", "lags", "waste", "doesn't work", "doesnt work", "problem",
                          "sucks"
                          "worst",
                          "pathetic", "not good", "not very good", "ineffective", "poor", "not success"]
        self.features = ["phone", "phones", "device", "camera", "fingerprint", "fingerprints", "finger lock", "display",
                         "design", "performance",
                         "screen", "photos", "pictures", "battery", "backup", "connectivity", "fingerlock",
                         "finger lock",
                         "finger", "speed",
                         "sound", "headset", "headphones", "speakers", "speaker", "charger", "water resistance",
                         "notifications light",
                         "super amoled", "adaptive brightness sensor", "call quality", "call", "nfc", "other devices",
                         "one ui",
                         "one-ui", "pubg", "games", "color", "water", "bluetooth", "ram", "images", "gorrilla glass",
                         "heating",
                         "face recognition", "lowlight pictures", "lowlight"]

        print("Test : ", self.query)
        print("Test : ", self.pages)

        # creating trie
        self.trie = Trie()
        for pos in self.positives:
            self.trie.insert(pos, 'Positive')
        for neg in self.negatives:
            self.trie.insert(neg, 'Negative')
        for ftr in self.features:
            self.trie.insert(ftr, 'Features')

        self.excel = Excel()

        google = Google()
        # res stores the url of exact review page for amazon from where we have to scrape data
        url = google.search(self.query)
        print("testing class : ", url[0])
        print("type of res[0]", type(url[0]))

        page_soup = self.getPageSoup(url[0])
        self.getAnalysisData(page_soup)

        for i in range(1, self.pages):
            url = self.nextPageURL(page_soup)
            print("new url : ", url)
            page_soup = self.getPageSoup(url)
            self.getAnalysisData(page_soup)

        self.excel.closeExcel()


    def getPageSoup(self, link):
        page = requests.get(link)
        page_html = page.text
        page_soup = soup(page_html, "html.parser")
        return page_soup

    def nextPageURL(self, page_soup):
        for a in page_soup.select("li.a-last a"):
            # print(a.get('href'))
            half_url = a.get('href')
            new_url = "http://www.amazon.in" + half_url

            print(new_url)
            return new_url

    def getAnalysisData(self, page_soup):
        # COMMENTS
        reviews_list = []
        all_reviews = page_soup.findAll("a", {"data-hook": "review-title"})
        for r in all_reviews:
            reviews_list.append(str(r.text).strip().lower())

        # RATINGS
        ratings_list = []
        ratings = page_soup.findAll("span", {"class": "a-icon-alt"})
        for r in ratings:
            rate = list(str(r.text).strip().split(" "))
            rate = (rate[0] + "/" + rate[3])
            ratings_list.append(rate)

        # DATE
        date_list = []
        dates = page_soup.findAll("span", {"class": "a-size-base a-color-secondary review-date"})
        for d in dates:
            # can create a function which formats all the dates in same format
            # print(d.text)
            date_list.append(d.text)

        # COMMENTS
        comments_list = []
        comments = page_soup.findAll("span", {"class": "a-size-base review-text review-text-content"})
        comments = str(comments)
        comments = comments.replace("<br/>", " ")
        newsoup = soup(comments, 'html.parser')
        comments = newsoup.findAll("span", {"data-hook": "review-body"})

        for c in comments:
            curr_comment = str(c.text).strip()
            curr_comment = curr_comment.lower()
            # print(curr_comment)
            comments_list.append(curr_comment)

        print("Comment List Lenght : ", len(reviews_list))
        print("Rating List Length : ", len(ratings_list))
        for i in range(len(reviews_list)):
            print((i+1), ratings_list[i], reviews_list[i])
        # for i in range(len(reviews_list)):
        #     sentiment_value = TextBlob(comments_list[i]).sentiment.polarity
        #     self.getInfoOfComment(comments_list[i])
        #     positive_points, negative_points, pos_ftrs, neg_ftrs, all_ftrs = self.getInfoOfComment(comments_list[i])
        #
        #     data_dict = {'review-title': reviews_list[i],
        #                  'user-ratings': ratings_list[i],
        #                  'date': date_list[i],
        #                  'comment': comments_list[i],
        #                  'sentiment-value': sentiment_value,
        #                  'all-features': all_ftrs,
        #                  'positive-features': pos_ftrs,
        #                  'positive-points': positive_points,
        #                  'negative-features': neg_ftrs,
        #                  'negative-points': negative_points,
        #                  }
        #
        #     print(data_dict)
        #
        #     # createFile(data_dict)
        #     self.excel.insertRow(reviews_list[i], date_list[i], ratings_list[i], sentiment_value,
        #                    set(all_ftrs), set(pos_ftrs), positive_points, set(neg_ftrs), negative_points)
        #
        #     print("\n")

    def getInfoOfComment(self, comment):
        comment_tokens = re.split("(\.|\s|\,)+", comment)
        comment = ""
        for token in comment_tokens:
            token = token.strip()
            # print(token, len(token))
            if token.isalpha():
                comment = comment + token + " "

        comment = comment.strip()

        curr_all = []
        curr_features = []
        curr_positives = []
        curr_negatives = []

        # data in strings
        positive_feature = []
        negative_feature = []
        positive_points = []
        negative_points = []
        string_features = []

        cmt = comment
        cmtInList = cmt.split(" ")
        end = len(cmt)
        i = 0
        word_id = 1
        while i < end:
            if not self.trie.suffixSearch3(cmt[i:end], self.trie.root).match:
                i += 1
            else:
                matchnode = self.trie.suffixSearch3(cmt[i:end], self.trie.root)
                if matchnode.polarity == 'Positive':
                    print(matchnode.polarity)
                    inCommentIndex = len(cmt[0:i].split(" "))
                    # polarity = matchnode.polarity
                    newNode = Node(matchnode.matchString, cmt[i:end].index(matchnode.matchString) + i, word_id,
                                   inCommentIndex, "Positive")
                    # curr_positives.append(Node(matchnode.matchString, cmt[i:end].index(matchnode.matchString)+i, word_id))
                    curr_positives.append(newNode)
                    curr_all.append(newNode)
                    word_id += 1
                elif matchnode.polarity == 'Negative':
                    inCommentIndex = len(cmt[0:i].split(" "))
                    newNode = Node(matchnode.matchString, cmt[i:end].index(matchnode.matchString) + i, word_id,
                                   inCommentIndex, "Negative")
                    curr_negatives.append(newNode)
                    curr_all.append(newNode)
                    word_id += 1
                elif matchnode.polarity == 'Features':
                    inCommentIndex = len(cmt[0:i].split(" "))
                    newNode = Node(matchnode.matchString, cmt[i:end].index(matchnode.matchString) + i, word_id,
                                   inCommentIndex, "Features")
                    curr_features.append(newNode)
                    string_features.append(str(newNode.data))
                    curr_all.append(newNode)
                    word_id += 1
                i += matchnode.matchLen
        # print("All : ", curr_all)

        # printing bullet points
        for id in range(len(curr_all)):
            if curr_all[id].polarity == "Features":
                # special case when negative word is just right behind the feature
                if id - 1 >= 0 and curr_all[id - 1].polarity == "Negative" and curr_all[id - 1].visited == False:
                    if curr_all[id].inCommentIndex - curr_all[id - 1].inCommentIndex == 1:
                        curr_all[id].visited = True
                        curr_all[id - 1].visited = True
                        result = ' '.join(
                            w for w in cmtInList[curr_all[id - 1].inCommentIndex - 1: curr_all[id].inCommentIndex - 1])
                        result = result + " " + curr_all[id].data
                        negative_points.append(result)
                        negative_feature.append(curr_all[id].data)
                        print(curr_all[id].data, " -> ", result)

                # special case when positive word is just right behind the feature
                elif id - 1 >= 0 and curr_all[id - 1].polarity == "Positive" and curr_all[id - 1].visited == False:
                    if curr_all[id].inCommentIndex - curr_all[id - 1].inCommentIndex == 1:
                        curr_all[id].visited = True
                        curr_all[id - 1].visited = True
                        result = ' '.join(
                            w for w in cmtInList[curr_all[id - 1].inCommentIndex - 1: curr_all[id].inCommentIndex - 1])
                        result = result + " " + curr_all[id].data
                        positive_points.append(result)
                        positive_feature.append(curr_all[id].data)
                        print(curr_all[id].data, " -> ", result)


                # if next word is negative and within threshold limit... print
                elif id + 1 < len(curr_all) and curr_all[id + 1].polarity == "Negative" and curr_all[
                    id + 1].visited == False:
                    if curr_all[id + 1].inCommentIndex - curr_all[id].inCommentIndex <= 5:
                        curr_all[id + 1].visited = True
                        curr_all[id].visited = True
                        result = ' '.join(
                            w for w in cmtInList[curr_all[id].inCommentIndex - 1: curr_all[id + 1].inCommentIndex - 1])
                        result = result + " " + curr_all[id + 1].data
                        negative_points.append(result)
                        negative_feature.append(curr_all[id + 1].data)
                        print(curr_all[id].data, " -> ", result)

                # if next word is positive and within threshold limit... print
                elif id + 1 < len(curr_all) and curr_all[id + 1].polarity == "Positive" and curr_all[
                    id + 1].visited == False:
                    if curr_all[id + 1].inCommentIndex - curr_all[id].inCommentIndex <= 5:
                        curr_all[id + 1].visited = True
                        curr_all[id].visited = True
                        result = ' '.join(
                            w for w in cmtInList[curr_all[id].inCommentIndex - 1: curr_all[id + 1].inCommentIndex - 1])
                        result = result + " " + curr_all[id + 1].data
                        positive_points.append(result)
                        positive_feature.append(curr_all[id + 1].data)
                        print(curr_all[id].data, " -> ", result)

        return positive_points, negative_points, positive_feature, negative_feature, string_features


amazonObj = AmazonUtil("Samsung a50 product-reviews Amazon india", 5)