import pandas as pd


def proportionBySport(data, year, sport, sex):
    allbysex = len(data.loc[data['Year'] == year].loc[data['Sex'] == sex])
    spbysex = len(data.loc[data['Year'] == year].loc[data['Sex'] == sex].loc[data['Sport'] == sport])
    return spbysex / allbysex
