import numpy as np
from ImageProcessor import ImageProcessor as ip
from AdvancedFilter import AdvancedFilter as af

i = ip()
af = af()

img = i.load("../resources/42AI.png")
print("Image :")
i.display(img)
print("gaussian_blur :")
i.display(af.gaussian_blur(img))
print("mean_blur :")
i.display(af.mean_blur(img))
