from Trie import *
import re
from textblob import TextBlob
import nltk

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

class Sentiment:
    def __init__(self):
        self.positives = ["good", "gud", "well", "great", "decent", "amazing", "excellent", "sexy", "superb", "suburb",
                          "awesome", "awsm", "nice", "happy", "high", "average",
                          "fast", "quick", "immersing", "immersive", "premium",
                          "best", "better",
                          "perfect", "perfection", "beast", "great", "fantastic", "faster", " fabulous", "blazing",
                          "loved", "love",
                          "marvellous", "comfortable", "unbeatable"
                          "charge", "smooth", "beautifully", "beautiful", "superb"]
        self.negatives = ["very bad", "bad", "disappointment", "wrong", "never", "slow", "no", "not good", "not work",
                          "not", "terrible", "heavy"
                          "issue", "defect", "slowest", "lags", "waste", "doesn't work",
                          "doesnt work", "doesnt", "doesn't",
                          "problem", "sucks", "worst",
                          "pathetic", "not good", "not very good", "ineffective", "poor", "not success"]
        self.features = ["phone", "phones", "device", "product", "mobile", "look",
                         "front camera", "back camera", "rear camera", "camera", "selfie", "front",
                         "photos", "pictures", "video", "images", "lowlight pictures", "lowlight",
                         "fingerprint", "fingerprints", "finger print", "finger lock", "fingerlock", "finger", "touch",
                         "display", "hd", "design", "build", "performance", "gorilla glass", "screen", "super amoled",
                         "amoled", "notch", "gorrilla glass",
                         "battery", "backup", "charging", "charge", "charger",
                         "connectivity", "network",
                         "face unlock", "face", "face recognition",
                         "sound", "headset", "headphones", "audio", "speakers", "speaker",
                         "water resistance", "water",
                         "notifications light", "notification light",
                         "adaptive brightness sensor", "sensor", "call quality", "call", "nfc", "wifi", "bluetooth",
                         "other devices",
                         "one ui", "one-ui", "ui", "os", "color os", "coloros", "miui",
                         "pubg", "gaming", "games", "color", "ram", "memory",
                         "heating", "price", "cost", "value for money", "budget", "affordable",
                         "processor", "chipset", "cpu", "speed", "bloatware",
                         "microsd", "micro sd", "storage",
                         "weight"]

        # STOPWORDS
        self.stopwords = nltk.corpus.stopwords.words('english')
        for pos in self.positives:
            if pos in self.stopwords:
                self.stopwords.remove(pos)
        for neg in self.negatives:
            if neg in self.stopwords:
                self.stopwords.remove(neg)
        for ftr in self.features:
            if ftr in self.stopwords:
                self.stopwords.remove(ftr)

        self.trie = Trie()
        for pos in self.positives:
            self.trie.insert(pos, 'Positive')
        for neg in self.negatives:
            self.trie.insert(neg, 'Negative')
        for ftr in self.features:
            self.trie.insert(ftr, 'Features')

    def sentimentAnalysis(self, comment):
        comment_tokens = re.split("(\.|\s|\,|\n)+", comment)
        comment_tokens = [re.sub(r"\W+|\d+", "", ct) for ct in comment_tokens if ct!=" "]
        comment = ""
        for token in comment_tokens:
            token = token.strip()
            if token != "":
                comment = comment + token + " "

        comment = comment.strip().lower()

        curr_all = []
        curr_features = []
        curr_positives = []
        curr_negatives = []

        # data in strings
        all_features_set = set()    # stores all the features present in the comment <dataype:string>
        positive_feature = []
        negative_feature = []
        positive_points = []
        negative_points = []
        string_features = []

        cmt = comment
        # print(cmt)
        sentiment_value = TextBlob(cmt).sentiment.polarity
        cmtInList = cmt.split(" ")
        end = len(cmt)
        i = 0
        word_id = 1

        while i < end:
            # print("BEFORE : ", cmt[i:])
            if not self.trie.suffixSearch3(cmt[i:end], self.trie.root).match:
                i += 1
            else:
                matchnode = self.trie.suffixSearch3(cmt[i:end], self.trie.root)
                if matchnode.polarity == 'Positive':
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
                    all_features_set.add(newNode.data)
                    string_features.append(str(newNode.data))
                    curr_all.append(newNode)
                    word_id += 1
                i += matchnode.matchLen + 2
                # print(matchnode.matchString, matchnode.matchLen)
            # print("AFTER : ", cmt[i:])

        # print("All : ", curr_all)
        # print("Feaures : ", curr_features)
        # print("Positives : ", curr_positives)
        # print("Negatives : ", curr_negatives)


        positive_feature_set = set()
        negative_feature_set = set()


        # printing bullet points
        for id in range(len(curr_all)):
            if curr_all[id].polarity == "Features":
                ########### new code start ##########
                pos_neg = ""
                min_distance = 100
                case = 0 # declaration

                # problem with case 1 is it doesnot maitain
                if id - 1 >= 0 and curr_all[id - 1].polarity == "Negative" and curr_all[id - 1].visited == False:
                    if self.Distance1(cmtInList, curr_all, id) < min_distance:
                        if min(self.Distance1(cmtInList, curr_all, id), min_distance) == 1:
                            min_distance = min(self.Distance1(cmtInList, curr_all, id), min_distance)
                        # print("CASE 1 : ", curr_all[id].data, curr_all[id-1].data, min_distance)
                        pos_neg = "Negative -> " + curr_all[id - 1].data
                        case = 1
                elif id - 1 >= 0 and curr_all[id - 1].polarity == "Positive" and curr_all[id - 1].visited == False:
                    if self.Distance1(cmtInList, curr_all, id) < min_distance:
                        if min(self.Distance1(cmtInList, curr_all, id), min_distance) == 1:
                            min_distance = min(self.Distance1(cmtInList, curr_all, id), min_distance)
                        # print("CASE 2 : ", curr_all[id].data, curr_all[id-1].data, min_distance)
                        pos_neg = "Positive -> " + curr_all[id - 1].data
                        case = 2
                if id + 1 < len(curr_all) and curr_all[id + 1].polarity == "Negative" and curr_all[
                    id + 1].visited == False:
                    if self.Distance2(cmtInList, curr_all, id) < min_distance:
                        min_distance = min(self.Distance2(cmtInList, curr_all, id), min_distance)
                        # print("CASE 3 : ", curr_all[id].data, curr_all[id+1].data, min_distance)
                        pos_neg = "Negative -> " + curr_all[id + 1].data
                        case = 3
                elif id + 1 < len(curr_all) and curr_all[id + 1].polarity == "Positive" and curr_all[
                    id + 1].visited == False:
                    if self.Distance2(cmtInList, curr_all, id) < min_distance:
                        pos_neg = "Positive -> " + curr_all[id + 1].data
                        min_distance = min(self.Distance2(cmtInList, curr_all, id), min_distance)
                        # print("CASE 4 : ", curr_all[id].data, curr_all[id + 1].data, min_distance)
                        case = 4
                # print("Feature : ", curr_all[id].data, "\tPOS_NEG:", pos_neg)
                ########### new code end ##########

                # special case when negative word is just right behind the feature
                # print("Feature : ", curr_all[id].data)
                # if id - 1 >= 0 and curr_all[id - 1].polarity == "Negative" and curr_all[id - 1].visited == False:
                if case == 1:
                    # print("\t", "Negative : ", curr_all[id - 1].data, "\tVisited :", curr_all[id - 1].visited, "\tDistance: ", self.Distance1(cmtInList, curr_all, id))
                    if self.Distance1(cmtInList, curr_all, id) == 1:
                    # if curr_all[id].inCommentIndex - curr_all[id - 1].inCommentIndex == 1:
                        curr_all[id].visited = True
                        curr_all[id - 1].visited = True
                        result = ' '.join(
                            w for w in cmtInList[curr_all[id - 1].inCommentIndex - 1: curr_all[id].inCommentIndex - 1])
                        result = result + " " + curr_all[id].data
                        negative_points.append(result)
                        negative_feature.append(curr_all[id].data)
                        negative_feature_set.add(str(curr_all[id].data))
                        # print(curr_all[id].data, " -> ", result)

                # special case when positive word is just right behind the feature
                # elif id - 1 >= 0 and curr_all[id - 1].polarity == "Positive" and curr_all[id - 1].visited == False:
                elif case == 2:
                    if self.Distance1(cmtInList, curr_all, id) == 1:
                    # if curr_all[id].inCommentIndex - curr_all[id - 1].inCommentIndex == 1:
                        curr_all[id].visited = True
                        curr_all[id - 1].visited = True
                        result = ' '.join(
                            w for w in cmtInList[curr_all[id - 1].inCommentIndex - 1: curr_all[id].inCommentIndex - 1])
                        result = result + " " + curr_all[id].data
                        positive_points.append(result)
                        positive_feature.append(curr_all[id].data)
                        positive_feature_set.add(curr_all[id].data)
                        # print(curr_all[id].data, " -> ", result)


                # if next word is negative and within threshold limit... print
                # elif id + 1 < len(curr_all) and curr_all[id + 1].polarity == "Negative" and curr_all[
                #     id + 1].visited == False:
                elif case == 3:
                    if self.Distance2(cmtInList, curr_all, id) <= 5:
                    # if curr_all[id + 1].inCommentIndex - curr_all[id].inCommentIndex <= 5:
                        curr_all[id + 1].visited = True
                        curr_all[id].visited = True
                        result = ' '.join(
                            w for w in cmtInList[curr_all[id].inCommentIndex - 1: curr_all[id + 1].inCommentIndex - 1])
                        result = result + " " + curr_all[id + 1].data
                        negative_points.append(result)
                        negative_feature.append(curr_all[id + 1].data)
                        negative_feature_set.add(curr_all[id].data)
                        # print(curr_all[id].data, " -> ", result)

                # if next word is positive and within threshold limit... print
                # elif id + 1 < len(curr_all) and curr_all[id + 1].polarity == "Positive" and curr_all[
                #     id + 1].visited == False:
                elif case == 4:
                    if self.Distance2(cmtInList, curr_all, id) <= 5:
                    # if curr_all[id + 1].inCommentIndex - curr_all[id].inCommentIndex <= 5:
                        curr_all[id + 1].visited = True
                        curr_all[id].visited = True
                        result = ' '.join(
                            w for w in cmtInList[curr_all[id].inCommentIndex - 1: curr_all[id + 1].inCommentIndex - 1])
                        result = result + " " + curr_all[id + 1].data
                        positive_points.append(result)
                        positive_feature.append(curr_all[id + 1].data)
                        positive_feature_set.add(curr_all[id].data)
                        # print(curr_all[id].data, " -> ", result)


        # print("Positive Points : ", positive_points)
        # print("Negative Points : ", negative_points)
        # print("All Featues set : ", all_features_set)
        # print("POSITIVE SET : ", positive_feature_set)
        # print("NEGATIVE SET : ", negative_feature_set)

        return sentiment_value, all_features_set, positive_feature_set, positive_points, negative_feature_set, negative_points

    def Distance1(self, cmtInList, curr_all, id):
        distance = curr_all[id].inCommentIndex - curr_all[id - 1].inCommentIndex
        tokens = cmtInList[curr_all[id - 1].inCommentIndex - 1: curr_all[id].inCommentIndex - 1]
        substract = 0
        for tt in tokens:
            if tt in self.stopwords:
                substract += 1

        return distance-substract

    def Distance2(self, cmtInList, curr_all, id):
        distance = curr_all[id + 1].inCommentIndex - curr_all[id].inCommentIndex
        tokens = cmtInList[curr_all[id].inCommentIndex - 1: curr_all[id + 1].inCommentIndex - 1]
        substract = 0
        for tt in tokens:
            if tt in self.stopwords:
                substract += 1

        return distance - substract


# comment = "It's a nice phone with great features, and value for money"
# print(comment)
# sn = Sentiment()
# sn.sentimentAnalysis(comment)
