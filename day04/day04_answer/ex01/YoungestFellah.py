import pandas as pd


def youngestFellah(data, year):
    d = data.loc[data['Year'] == year]
    m = d.loc[d['Sex'] == "M"]
    f = d.loc[d['Sex'] == "F"]
    dic = {}
    dic['f'] = f['Age'].min()
    dic['m'] = m['Age'].min()
    return dic
