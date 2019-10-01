import pandas as pd
import re

class Controller:
    def __init__(self, filename, sheetname, feature, polarity):
        self.filename = filename
        self.feature = feature
        self.polarity = polarity
        self.sheetname = sheetname

    def getResults(self):
        comment_list = []
        dataframe = pd.read_excel(self.filename, sheet_name=self.sheetname)  # <type:dataframe>
        rows, cols = dataframe.shape
        dictionary = {"phone": ["phone", "device"],
                           "camera": ["camera", "photos", "picture"],
                           "battery": ["battery", "backup"],
                           "display": ["display", "screen"],
                           "finger": ["finger"]}

        all_features = dataframe["All Features Apperared"]
        comments = dataframe["Comment"]

        if self.polarity == "ALL":
            comment_list = []
            for i in range(rows):
                for ftr in dictionary[self.feature]:
                    if str(all_features[i]).__contains__(ftr):
                        string = comments[i].encode('ascii', 'ignore').decode('ascii')

                        comment_list.append(string)
                        break

            return comment_list


        elif self.polarity == "Positive":
            pass

        elif self.polarity == "Negative":
            pass

        elif self.polarity == "Uncategorized":
            pass


