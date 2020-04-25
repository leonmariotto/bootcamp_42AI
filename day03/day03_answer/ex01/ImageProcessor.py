import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class ImageProcessor():
  def __init__(self):
    pass

  def load(self, path):
    img = mpimg.imread(path)
    if img.dtype == np.float32: # Si le résultat n'est pas un tableau d'entiers
      img = (img * 255).astype(np.uint8)
    print("Image loaded :", img.shape)
    return img

  def display(self, array):
    plt.imshow(array)
    plt.show()
