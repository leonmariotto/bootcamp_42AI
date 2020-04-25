import pandas as pd

class SpatioTemporalData():
    def __init__(self, data):
        self.data = data

    def where(self, year):
        return pd.unique(self.data[self.data['Year'] == year].City)
        #list_place = []
        #datay = self.data[self.data['Year'] == year]
        #for i, row in datay.iterrows():
        #    if row['City'] not in list_place:
        #        list_place.append(row['City'])
        #return list_place

    def when(self, city):
        return pd.unique(self.data[self.data['City'] == city].Year)
        #list_year = []
        #datay = self.data[self.data['City'] == city]
        #for i, row in datay.iterrows():
        #    if row['Year'] not in list_year:
        #        list_year.append(row['Year'])
        #return list_year
            
