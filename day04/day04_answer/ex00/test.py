from FileLoader import *
loader = FileLoader()
print("Bad file name :")
data = loader.load('../resources/testtruc.csv')
print("Good file name :")
data = loader.load('../resources/athlete_events.csv')
print("5 premieres lignes :")
loader.display(data, 5)
print("5 dernieres lignes :")
loader.display(data, -5)