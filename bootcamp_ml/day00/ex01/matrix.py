from vector import Vector


class Matrix():
    def __init__(self, data, shape=(0, 0)):
        if type(data) is list and type(data[0]) is list:
            nrow = len(data)
            ncol = len(data[0])
#            self.data = [[float(i)] * ncol for j in data]
#            self.data = [float(i) for j in data for i in j]
            self.data = data
            for i in self.data:
                for j in i:
                    j = float(j)
            if shape != (0, 0) and shape != (nrow, ncol):
                raise ValueError("Data shape and shape are not same\n")
            self.shape = (nrow, ncol)
        elif type(data) is tuple:
            self.data = [[float(0)] * data[1] for i in range(data[0])]
            self.shape = data

    def __add__(self, num):
        new = Matrix((self.shape))
        if type(num) is int or type(num) is float:
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new.data[i][j] = self.data[i][j] + num
        elif type(num) is Matrix:
            if num.shape != self.shape:
                raise ValueError("Shapes are not same")
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new.data[i][j] = self.data[i][j] + num.data[i][j]
        return new

    def __radd__(self, num):
        return self.__add__(num)

    def __sub__(self, num):
        new = Matrix((self.shape))
        if type(num) is int or type(num) is float:
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new.data[i][j] = self.data[i][j] - num
        elif type(num) is Matrix:
            if num.shape != self.shape:
                raise ValueError("Shapes are not same")
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new.data[i][j] = self.data[i][j] - num.data[i][j]
        return new

    def __rsub__(self, num):
        new = Matrix((self.shape))
        if type(num) is int or type(num) is float:
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new.data[i][j] = num - self.data[i][j]
        elif type(num) is Matrix:
            if num.shape != self.shape:
                raise ValueError("Shapes are not same")
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new.data[i][j] = num.data[i][j] - self.data[i][j]
        return new

    def __truediv__(self, num):
        new = Matrix((self.shape))
        if type(num) is int or type(num) is float:
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    try:
                        new.data[i][j] = self.data[i][j] / num
                    except ZeroDivisionError:
                        new.data[i][j] = "Error"
        return new

    def __rtruediv__(self, num):
        new = Matrix((self.shape))
        if type(num) is int or type(num) is float:
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    try:
                        new.data[i][j] = num / self.data[i][j]
                    except ZeroDivisionError:
                        new.data[i][j] = "Error"
        return new

    def __mul__(self, num):
        if type(num) is int or type(num) is float:
            new = Matrix((self.shape))
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new.data[i][j] = self.data[i][j] * num
        elif type(num) is Vector:
            if num.size != self.shape[1]:
                raise ValueError("Matrix and Vector not compatibles")
            new = Vector(num.size)
            for i in range(self.shape[0]):
                new.value[i] = 0
                for j in range(self.shape[1]):
                    new.value[i] += self.data[i][j] * num.value[j]
        elif type(num) is Matrix:
            if self.shape[1] != num.shape[0]:
                raise ValueError("Matrixs not compatibles")
            new = Matrix((self.shape[0], num.shape[1]))
            for k in range(num.shape[1]):
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        new.data[i][k] += self.data[i][j] * num.data[j][k]
        return new

    def __str__(self):
        s = "Matrix = [\n"
        for l in self.data:
            s += str(l)
            s += ",\n"
        s += "]"
        return s

    def __repr__(self):
        s = "[\n"
        for l in self.data:
            s += str(l)
            s += ",\n"
        s += "]"
        return s
