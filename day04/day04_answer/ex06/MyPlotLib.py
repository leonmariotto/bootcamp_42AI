import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def parse_features(features, data):
    good_features = []
    for elem in features:
        if elem in data:
            try:
                t = data[elem] + 1
            except TypeError:
                pass
            else:
                good_features.append(elem)
    if good_features == []:
        return False
    return good_features
    
class MyPlotLib():
    def __init__(self):
        pass

    def histogram(self, data, features):
        good_features = parse_features(features, data)
        l = len(good_features)
        f = plt.figure(1)
        data = data.fillna(data.median())
        for i, feature in enumerate(good_features):
            a = plt.subplot(1, l, i + 1)
            a.hist(data[feature], color='blue', edgecolor='black',
                   bins = 30)
            a.title.set_text(feature)
        plt.subplots_adjust(wspace=1)
        plt.show()
        return True

    def density(self, data, features):
        good_features = parse_features(features, data)
        f = plt.figure(1)
        data = data.fillna(data.median())
        for elem in good_features:
            subset = data[elem]
            sns.distplot(subset, hist=False, kde=True, kde_kws={'linewidth': 3},
                         label = elem)
        plt.show()
        return True

    def pair_plot(self, data, features):
        good_features = parse_features(features, data)
        data = data[features]
        data = data.fillna(data.median())
        sns.set(style="ticks", color_codes=True)
        sns.pairplot(data)
        plt.show()
        return True

    def box_plot(self, data, features):
        good_features = parse_features(features, data)
        l = len(good_features)
        data = data.fillna(data.median())
        f, plo = plt.subplots(1, l, sharey=True, squeeze=False)
        for i, feature in enumerate(good_features):
            plo[0, i].boxplot(data[feature])
            plo[0, i].title.set_text(feature)
        plt.subplots_adjust(wspace=1)
        plt.show()
        return True

