from ImageProcessor import ImageProcessor as ip
from ScrapBooker import ScrapBooker as scbook
import numpy as np

i = ip()

img = i.load("../resources/42AI.png")
s = scbook()

print("\n\n\ntest juxtapose horizontal :\n")
i.display(s.juxtapose(img, 3, 1))
print("\n\n\ntest juxtapose vertical :\n")
i.display(s.juxtapose(img, 3, 0))
print("\n\n\ntest crop \n")
i.display(s.crop(img, (100,100)))
print("\n\n\ntest mosaic horizontal :\n")
i.display(s.mosaic(img, (2,3)))
print("\n\n\ntest mosaic vertical :\n")
i.display(s.mosaic(img, (3,2)))
print("\n\n\ntest thin horizontal :\n")
i.display(s.thin(img, 2, 1))
print("\n\n\ntest thin vertical :\n")
i.display(s.thin(img, 2, 0))
#print("\n\n\ntest thin horizontal :\n")
#print(s.thin(test, 5, 1))
#print("\n\n\ntest thin verticak :\n")
#print(s.thin(test, 2, 0))

#print("\n\n\ntest thin horizontal :\n")
#i.display(s.thin(img, 2, 1))
#print("\n\n\ntest thin horizontal :\n")
#i.display(s.thin(img, 3, 1))
#print("\n\n\ntest thin horizontal :\n")
#i.display(s.thin(img, 4, 1))
#print("\n\n\ntest thin horizontal :\n")
#i.display(s.thin(img, 5, 1))
#print("\n\n\ntest thin horizontal :\n")
#i.display(s.thin(img, 6, 1))
