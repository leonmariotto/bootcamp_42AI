import random
import numpy

class NumPyCreator():
  def __init__(self):
    pass

  def from_list(self, lst):
    return numpy.array(lst)

  def from_tuple(self, tup):
    return numpy.array(tup)

  def from_shape(self, shape, value=0):
    self.data = [[value for x in range(shape[1])] for x in range(shape[0])]
    return numpy.array(self.data)

  def random(self, shape):
    self.data = [[random.random() for x in range(shape[1])] for x in range(shape[0])]
    return numpy.array(self.data)

  def identity(self, size):
    self.data = [[0 for x in range(size)] for x in range(size)]
    c = 0
    for i, elem in enumerate(self.data):
      elem[c] = 1
      c += 1
    return numpy.array(self.data)
    