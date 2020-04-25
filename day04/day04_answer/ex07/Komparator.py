import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class Komparator():
    def __init__(self, data):
        self.data = data

    def compare_box_plots(self, categorical_var, numerical_var):
        poss_value = pd.unique(self.data[categorical_var])
        self.data = self.data.fillna(self.data.median())
        f, plo = plt.subplots(1, len(poss_value), sharey=True, squeeze=False)
        for i, value in enumerate(poss_value):
            tmp = self.data.loc[self.data[categorical_var] == value]
            plo[0, i].boxplot(tmp[numerical_var])
            plo[0, i].title.set_text("{:s} of {:s}".format(numerical_var, value))
        plt.subplots_adjust(wspace=0.8)
        plt.show()
        return True
    
    def density(self, categorical_var, numerical_var):
        poss_value = pd.unique(self.data[categorical_var])
        self.data = self.data.fillna(self.data.median())
        f = plt.figure(1)
        for i, value in enumerate(poss_value):
            tmp = self.data.loc[self.data[categorical_var] == value]
            sns.distplot(tmp[numerical_var], hist=False, kde=True, kde_kws={'linewidth': 3}, label = value)
        plt.show()
        return True

    def compare_histograms(self, categorical_var, numerical_var):
        poss_value = pd.unique(self.data[categorical_var])
        self.data = self.data.fillna(self.data.median())
        f, plo = plt.subplots(1, len(poss_value), sharey=True, squeeze=False)
        for i, value in enumerate(poss_value):
            tmp = self.data.loc[self.data[categorical_var] == value]
            plo[0, i].hist(tmp[numerical_var], color='red', edgecolor='black')
            plo[0, i].title.set_text("{:s} of {:s}".format(numerical_var, value))
        plt.subplots_adjust(wspace=0.8)
        plt.show()
        return True
        
