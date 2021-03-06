import numpy as np

class AdvancedFilter:
    def __init__(self):
        pass

    def mean_blur(self, array):
        arr = np.array(array)
        m, n, p = arr.shape
        size = 3
        mm, nn = m - size + 1, m - size + 1
        patch_means = np.empty((mm, nn, p))
        for i in range(mm):
            for j in range(nn):
                im = int(i - (size - 1) / 2)
                ip = int(i + (size - 1) / 2)
                jp = int(j + (size - 1) / 2)
                jm = int(j - (size - 1) / 2)
                if im < 0:
                    im = 0
                if jm < 0:
                    jm = 0
                patch_means[i, j] = arr[im: ip, jm: jp].mean(axis=0).mean(axis=0)
        return patch_means

    def gaussian_blur(self, array):
        arr = np.array(array)
        m, n, p = arr.shape
        kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
        size = 3
        mm, nn = m - size + 1, m - size + 1
        patch_means = np.empty((mm, nn, p))
        for i in range(mm):
            for j in range(nn):
                tmp = arr[i: i+size, j: j+size] * kernel[:,:,None]
                patch_means[i, j] = np.array([tmp[:,:,0].sum() / 16, tmp[:,:,1].sum() / 16, tmp[:,:,2].sum() / 16])
        return patch_means
