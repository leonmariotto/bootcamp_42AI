import pandas as pd


def howManyMedals(dataset, name):
    dataset = dataset.loc[dataset['Name'] == name]
    res = {}
    for index, row in dataset.iterrows():
        if row['Year'] not in res:
            res[row['Year']] = {'G': 0, 'S': 0, 'B': 0}
        if type(row['Medal']) is str:
            res[row['Year']][row['Medal'][0]] += 1
    return res
