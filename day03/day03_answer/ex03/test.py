from ImageProcessor import ImageProcessor as ip
from ColorFilter import ColorFilter as cf
import numpy as np

i = ip()
c = cf()

img = i.load("../resources/42AI.png")

test = np.zeros((2, 2, 3))
#print(img.size)
#print("\n\nInvert_color :")
#print(c.invert(img))

print("Image :")
i.display(img)

print("\n\nInvert_color :")
i.display(c.invert(img))
img = i.load("../resources/42AI.png")

print("\n\nblue filter :")
i.display(c.to_blue(img))
img = i.load("../resources/42AI.png")

print("\n\nred filter :")
i.display(c.to_red(img))
img = i.load("../resources/42AI.png")

print("\n\ngreen filter :")
i.display(c.to_green(img))
img = i.load("../resources/42AI.png")

print("\n\nto_grayscale filter w:")
i.display(c.to_grayscale(img, 'w'))

img = i.load("../resources/42AI.png")

print("\n\nto_grayscale filter m:")
i.display(c.to_grayscale(img, 'm'))

#print("\n\n\ntest juxtapose horizontal :\n")
#print(s.juxtapose(test, 3, 1))
#print("\n\n\ntest juxtapose vertical :\n")
#print(s.juxtapose(test, 3, 0))

#print("\n\n\ntest mosaic horizontal :\n")
#i.display(s.mosaic(img, (2,3)))
#print("\n\n\ntest mosaic vertical :\n")
#i.display(s.mosaic(img, (1,3)))
#print("\n\n\ntest mosaic vertical :\n")
#i.display(s.mosaic(img, (3,7)))
#print(s.thin(test, 2, 1))
#print("\n\n\ntest thin horizontal :\n")
#print(s.thin(test, 3, 1))
#print("\n\n\ntest thin horizontal :\n")
#print(s.thin(test, 4, 1))
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
