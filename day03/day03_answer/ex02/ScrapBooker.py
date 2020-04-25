import numpy as np

class ScrapBooker():
  def __init__(self):
    pass

  def crop(self, array, dimensions, position=(0,0)):
    array = array[position[0]:dimensions[0], position[1]:dimensions[1]]
    return array

  def thin(self, array, n, axis):
    if axis == 0 or axis == 1:
        array = np.delete(array, slice(None, None, n), axis)
    else:
        raise ValueError("Axis must be 0 or 1")
    return (array)
    
  def juxtapose(self, array, n, axis):
    if axis < 0 or axis > 1:
        raise ValueError("Axis must be 0 or 1")
    array = np.concatenate([array for i in range(n)], axis)
    return array

  def mosaic(self, array, dimensions):
    array = np.concatenate([array for i in range(dimensions[0])], 0)
    array = np.concatenate([array for i in range(dimensions[1])], 1)
    return array
