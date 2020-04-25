from FileLoader import FileLoader
from MyPlotLib import MyPlotLib
loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')
pl = MyPlotLib()
pl.histogram(data, ['Weight', 'Height'])
pl.density(data, ['Weight', 'Height'])
pl.pair_plot(data, ['Weight', 'Height'])
pl.box_plot(data, ['Weight', 'Height'])

#figure = plt.figure(figsize=(15,15))
#a = plt.subplot(1, 1, 1)
#a.hist(data['Height'], color='blue', edgecolor='black')
#a[1].hist(data['Weight'], color='blue', edgecolor='black', bins=int(180/5))

#plt.figure(1)
#a = plt.subplot(1, 2, 1)
#a.hist(data['Height'], color='blue', edgecolor='black')
#plt.subplot(1, 2, 2)
#b = plt.subplot(1, 2, 2)
#b.hist(data['Weight'], color='blue', edgecolor='black')
#b.title('Weight')
#
#plt.show()
