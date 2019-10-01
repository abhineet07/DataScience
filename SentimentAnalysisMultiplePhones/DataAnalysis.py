import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PolarityReport import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.axes.Axes.barh
matplotlib.pyplot.barh
matplotlib.axes.Axes.text
matplotlib.pyplot.text
matplotlib.axes.Axes.legend
matplotlib.pyplot.legend

class dataAnalysis:
    def __init__(self, filename, sheetname, modelname):
        self.filename = filename
        self.sheetname = sheetname
        self.modelname = modelname

    def generateWordCloud(self, polarity):
        pr = polarityReport(self.filename, self.sheetname, self.modelname)
        polarity_freq = pr.getPolarityDictionary(polarity)

        #Generating wordcloud. Relative scaling value is to adjust the importance of a frequency word.
        #See documentation: https://github.com/amueller/word_cloud/blob/master/wordcloud/wordcloud.py
        wordcloud = WordCloud(width=900,height=500, max_words=1628,relative_scaling=1,normalize_plurals=False).generate_from_frequencies(polarity_freq)

        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

    def generateBarGraph(self):
        pr = polarityReport(self.filename, self.sheetname, self.modelname)
        positive_polarity_freq = pr.getPolarityDictionary("Positive")
        negative_polarity_freq = pr.getPolarityDictionary("Negative")

        positive_polarity_list = list(positive_polarity_freq.values())
        negative_polarity_list = list(negative_polarity_freq.values())
        negative_polarity_list = [0-val for val in negative_polarity_list]
        # print(type(positive_polarity_list), (len(positive_polarity_list)))
        # print(positive_polarity_list)
        # print(type(negative_polarity_list), (len(negative_polarity_list)))
        # print(negative_polarity_list)

        feature_labels = list(positive_polarity_freq.keys())
        # print(feature_labels)

        x = range(len(positive_polarity_list))
        fig = plt.figure()
        ax = plt.subplot(111)
        ax.bar(x, negative_polarity_list, width=1, color='r')
        ax.bar(x, positive_polarity_list, width=1, color='b')

        rects = ax.patches
        for rect, label in zip(rects, feature_labels):
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
                    ha='center', va='bottom')
        plt.show()

    def fun2(self):
        pr = polarityReport(self.filename, self.sheetname, self.modelname)
        positive_polarity_freq = pr.getPolarityDictionary("Positive")
        negative_polarity_freq = pr.getPolarityDictionary("Negative")
        feature_labels = list(positive_polarity_freq.keys())

        category_names = ['Positive', 'Negative']
        new_dict = {}
        for i in range(len(feature_labels)):
            new_dict[feature_labels[i]] = [positive_polarity_freq[feature_labels[i]], negative_polarity_freq[feature_labels[i]]]

        my_plt = self.survey(new_dict, category_names)

    def survey(self, results, category_names):
        """
        Parameters
        ----------
        results : dict
            A mapping from question labels to a list of answers per category.
            It is assumed all lists contain the same number of entries and that
            it matches the length of *category_names*.
        category_names : list of str
            The category labels.
        """
        labels = list(results.keys())
        data = np.array(list(results.values()))
        data_cum = data.cumsum(axis=1)
        category_colors = plt.get_cmap('RdYlGn')(
            np.linspace(0.15, 0.85, data.shape[1]))

        fig, ax = plt.subplots(figsize=(9.2, 5))
        ax.invert_yaxis()
        ax.xaxis.set_visible(False)
        ax.set_xlim(0, np.sum(data, axis=1).max())

        for i, (colname, color) in enumerate(zip(category_names, category_colors)):
            widths = data[:, i]
            starts = data_cum[:, i] - widths
            ax.barh(labels, widths, left=starts, height=0.5,
                    label=colname, color=color)
            xcenters = starts + widths / 2

            r, g, b, _ = color
            text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
            for y, (x, c) in enumerate(zip(xcenters, widths)):
                ax.text(x, y, str(int(c)), ha='center', va='center',
                        color=text_color)
        ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
                  loc='lower left', fontsize='small')

        fig.show()
        # return fig, ax


# wc = wordcloudclass('Reviews_Samsung_m40.xlsx', 'Analysis', 'm10')
# wc.generateWordCloud('Negative')
# wc.generateBarGraph()