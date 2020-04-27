from FileLoader import FileLoader
from YoungestFellah import *
loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')
y = youngestFellah(data, 2004)
print(y)
