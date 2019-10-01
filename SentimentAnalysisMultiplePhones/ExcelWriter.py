import xlsxwriter

class Excel():
    def __init__(self):
        self.workbook = xlsxwriter.Workbook('Results.xlsx')
        self.worksheet = self.workbook.add_worksheet("Sheet-1")

        # cell_format = self.workbook.add_format({'bold': True})


        self.worksheet.set_default_row(height=70)
        # self.worksheet.set_column(width=50)

        self.worksheet.write(0, 0, "Review Title")
        self.worksheet.write(0, 1, "Date")
        self.worksheet.write(0, 2, "User Ratings")
        self.worksheet.write(0, 3, "Sentiment Value")
        self.worksheet.write(0, 4, "All Features")
        self.worksheet.write(0, 5, "Positive Features")
        self.worksheet.write(0, 6, "Positive Points")
        self.worksheet.write(0, 7, "Negative Features")
        self.worksheet.write(0, 8, "negative Points")

        # self.worksheet.set_row(0, 0, cell_format)

        self.index = 1

    def insertRow(self, reviewTitle, date, userRating, SentimentValue, AllFeatures,
                  PositiveFeatures, PositivePoints, NegativeFeatures, NegativePoints):
        self.worksheet.write(self.index, 0, reviewTitle)
        self.worksheet.write(self.index, 1, date)
        self.worksheet.write(self.index, 2, userRating)
        self.worksheet.write(self.index, 3, SentimentValue)

        custom_AllFeatures = '\n'.join(x for x in AllFeatures)
        self.worksheet.write(self.index, 4, custom_AllFeatures)

        custom_posFeatures = '\n'.join(x for x in PositiveFeatures)
        self.worksheet.write(self.index, 5, custom_posFeatures)

        custom_posPoints = '\n'.join(x for x in PositivePoints)
        self.worksheet.write(self.index, 6, custom_posPoints)

        custom_negFeatures = '\n'.join(x for x in NegativeFeatures)
        self.worksheet.write(self.index, 7, custom_negFeatures)

        custom_negPoints = '\n'.join(x for x in NegativePoints)
        self.worksheet.write(self.index, 8, custom_negPoints)

        self.index += 1

    def closeExcel(self):
        self.workbook.close()


# def insertData(i, reviewTitle, date, userRating, SentimentValue, AllFeatures,
#                 PositiveFeatures, PositivePoints, NegativeFeatures, NegativePoints):
#     row, column = 1, 1
#
#     # worksheet.write(0, 0, "Review Title")
#     # worksheet.write(0, 1, "Date")
#     # worksheet.write(0, 2, "User Ratings")
#     # worksheet.write(0, 3, "Sentiment Value")
#     # worksheet.write(0, 4, "All Features Discussed")
#     # worksheet.write(0, 5, "All Positive Features")
#     # worksheet.write(0, 6, "All Positive Points")
#     # worksheet.write(0, 7, "All Negative Features")
#     # worksheet.write(0, 8, "All Negative Points")
#
#     worksheet.write(i, 0, reviewTitle)
#     worksheet.write(i, 1, date)
#     worksheet.write(i, 2, userRating)
#     worksheet.write(i, 3, SentimentValue)
#
#     custom_AllFeatures = '\n'.join(x for x in AllFeatures)
#     worksheet.write(i, 4, custom_AllFeatures)
#
#     custom_posFeatures = '\n'.join(x for x in PositiveFeatures)
#     worksheet.write(i, 5, custom_posFeatures)
#
#     custom_posPoints = '\n'.join(x for x in PositivePoints)
#     worksheet.write(i, 6, custom_posPoints)
#
#     custom_negFeatures = '\n'.join(x for x in NegativeFeatures)
#     worksheet.write(i, 7, custom_negFeatures)
#
#     custom_negPoints = '\n'.join(x for x in NegativePoints)
#     worksheet.write(i, 8, custom_negPoints)
#
#     # for i in range(1, len(reviewTitle)):
#     #     worksheet.write(i, 0, reviewTitle[i])
#     #     worksheet.write(i, 1, date[i])
#     #     worksheet.write(i, 2, userRating[i])
#     #     worksheet.write(i, 3, SentimentValue)
#     #
#     #     custom_AllFeatures = '\n'.join(x for x in AllFeatures)
#     #     worksheet.write(i, 4, custom_AllFeatures)
#     #     worksheet.write(i, 5, PositiveFeatures[i])
#     #     worksheet.write(i, 6, PositivePoints[i])
#     #
#     #     worksheet.write(i, 7, NegativeFeatures[i])
#     #     worksheet.write(i, 8, NegativePoints[i])
#
#
# def closeExcel():
#     workbook.close()


