from FileLoader import FileLoader
from HowManyMedals import *
loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')
print(howManyMedals(data, 'Kjetil Andr Aamodt'))
