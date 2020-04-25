import pandas as pd


def howManyMedalsByCountry(dataset, cname):
    dataset = dataset.loc[dataset['Team'] == cname]
    res = {}
    for index, row in dataset.iterrows():
        if row['Year'] not in res:
            res[row['Year']] = {'G': 0, 'S': 0, 'B': 0}
        if type(row['Medal']) is str:
            res[row['Year']][row['Medal'][0]] += 1
    return res
