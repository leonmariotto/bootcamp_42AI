import numpy

class NumPyCreator():
  def __init__(self):
    pass

  def from_list(self, lst):
    if type(lst) is not list:
        raise TypeError
    return numpy.array(lst)

  def from_tuple(self, tup):
    if type(tup) is not tuple:
        raise TypeError
    return numpy.array(tup)

  def from_iterable(self, ite):
    return numpy.array(list(ite))

  def from_shape(self, shape, value=0):
    n = numpy.ones(shape)
    n *= value
    return n

  def random(self, shape):
    n = numpy.random.random_sample(shape)
    return n

  def identity(self, size):
    return numpy.identity(size)
