import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class ImageProcessor():
  def __init__(self):
    pass

  def load(self, path):
    img = mpimg.imread(path)
    print("Image loaded :", img.shape)
    img = img.astype(np.float32)
    return img

  def display(self, array):
    plt.imshow(array)
    plt.show()
