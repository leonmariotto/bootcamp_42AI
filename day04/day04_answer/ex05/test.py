from FileLoader import FileLoader
from HowManyMedalsByCountry import *
loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')
print(howManyMedalsByCountry(data, 'France'))
print(howManyMedalsByCountry(data, 'China'))
print(howManyMedalsByCountry(data, 'Germany'))
print(howManyMedalsByCountry(data, 'Spain'))
