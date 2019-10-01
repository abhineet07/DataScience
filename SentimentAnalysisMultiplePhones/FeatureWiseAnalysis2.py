import pandas as pd
import matplotlib.pyplot as plt

class featurewiseanalysis:
    def __init__(self, filename, sheetname):
        # dataframe = pd.read_excel(open('Flipkart.xlsx', 'rb'), index_col=0)
        self.dataframe = dfs = pd.read_excel(filename, sheet_name=sheetname)         # <type:dataframe>
        rows, cols = self.dataframe.shape
        self.dictionary = {"phone" : ["phone", "device"],
                           "camera" : ["camera", "photos", "picture"],
                           "battery" : ["battery", "backup"],
                           "display" : ["display", "screen", "notch", "amoled"],
                           "finger": ["finger"],
                           "price" : ["price", "cost", "value for money", "budget", "affordable"],
                           "performance" : ["performance", "perform", "sluggish", "lag", "hang"],
                           "face recognization" : ["face", "face unlock", "facial"],
                           "charging" : ["charge", "charging", "charger", "vooc"],
                           "design" : ["design", "look", "build"],
                           "call" : ["call"],
                           "heating" : ["heat", "heating"],
                           "game" : ["game", "pubg"],
                           "speaker" : ["speaker", "sound", "headphones"],
                           "ram" : ["ram", "memory"],
                           "bloatware" : ["bloatware"],
                           "ui" : ["ui", "one ui", "one-ui"]}


        # total_occured = dataframe["All Features Apperared"].apply(dataframe.count(lambda x : x.__contains__("finger")))

    def calculatePolarity(self, feature):
        relative_features = self.dictionary[feature]
        all_count = 0
        all_features = self.dataframe["All Features Apperared"]
        for af in all_features.dropna():
            for rf in relative_features:
                if af.__contains__(rf):
                    all_count += 1
                    break
        print("Total Occurance : ", all_count)

        positive_count = 0
        all_features = self.dataframe["Positive Feature Set"]
        for af in all_features.dropna():
            for rf in relative_features:
                if af.__contains__(feature):
                    positive_count += 1
                    break
        print("Positive : ", positive_count, "\t", (positive_count / all_count) * 100, "%")

        negative_count = 0
        all_features = self.dataframe["Negative Feature Set"]
        for af in all_features.dropna():
            if af.__contains__(feature):
                for rf in relative_features:
                    negative_count += 1
                    break
        print("Neagtive : ", negative_count, "\t", (negative_count / all_count) * 100, "%")

        return [all_count, positive_count, negative_count]

    # def calculatePolarity(self, feature):
    #     relative_features = self.dictionary[feature]
    #     all_count = 0
    #     all_features = self.dataframe["All Features Apperared"]
    #     for af in all_features.dropna():
    #         if af.__contains__(feature):
    #             all_count += 1
    #     print("Total Occurance : ", all_count)
    #
    #     positive_count = 0
    #     all_features = self.dataframe["Positive Feature Set"]
    #     for af in all_features.dropna():
    #         if af.__contains__(feature):
    #             positive_count += 1
    #     print("Positive : ", positive_count, "\t", (positive_count / all_count) * 100, "%")
    #
    #     negative_count = 0
    #     all_features = self.dataframe["Negative Feature Set"]
    #     for af in all_features.dropna():
    #         if af.__contains__(feature):
    #             negative_count += 1
    #     print("Neagtive : ", negative_count, "\t", (negative_count / all_count) * 100, "%")
    #
    #     return [all_count, positive_count, negative_count]

#
# positive_data = []
# negative_data = []
#
# fwa = featurewiseanalysis('Amazon.xlsx', 'Analysis')
# finger_all, finger_pos, finger_neg = fwa.calculatePolarity('finger')
# camera_all, camera_pos, camera_neg = fwa.calculatePolarity('camera')
# display_all, display_pos, display_neg = fwa.calculatePolarity('display')
# battery_all, battery_pos, battery_neg = fwa.calculatePolarity('battery')
#
# positive_data = [finger_pos, camera_pos, display_pos, battery_pos]
# negative_data = [0-finger_neg, 0-camera_neg, 0-display_neg, 0-battery_neg]
#
# x_labels = [u'Finger', u'Camera', u'Display', u'Battery']
# x = range(len(positive_data))
# fig = plt.figure()
# ax = plt.subplot(111)
# ax.set_xticklabels(x_labels, minor=False)
# ax.bar(x, positive_data, width=1, color='b')
# ax.bar(x, negative_data, width=1, color='r')
# plt.show()

#
# fwa = featurewiseanalysis('Reviews_Samsung_m10.xlsx', 'Analysis')
# fwa.calculatePolarity("ram")