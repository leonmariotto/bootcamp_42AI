import numpy as np

def vector_funk(a, thresholds):
    """ apply celluloid shade """
    b = np.linspace(0, 1, thresholds)
    for n in b:
        if n >= a:
            return n

class ColorFilter():
    def __init__(self):
        pass
    
    def invert(self, array):
        a = np.ones_like(array)
        return a - array
    
    def to_blue(self, array):
        a = np.array(array)
        a[:, :, :2] = 0
        return a
    
    def to_green(self, array):
        a = np.array(array)
        a[:, :, 0] = 0
        a[:, :, 2] = 0
        return a
    
    def to_red(self, array):
        a = np.array(array)
        a[:, :, 1:] = 0
        return a

    def celluloid(self, array, thresholds=4):
        a = np.array(array)
        vfunk = np.vectorize(vector_funk)
        return vfunk(a, thresholds)

    def to_grayscale(self, array, arg='weighted'):
        a = np.array(array)
        a = a.astype(np.float32) / 255
        if arg == 'weighted' or arg == 'w':
            a[:, :, 0] *= np.float32(0.299)
            a[:, :, 1] *= np.float32(0.587)
            a[:, :, 2] *= np.float32(0.114)
            return a
        elif arg == 'mean' or arg == 'm':
            newar = np.ones_like(a)
            for i, elem in enumerate(a):
                for j, ele in enumerate(elem):
                    newar[i, j] *= np.sum(ele) / 3
            return newar
