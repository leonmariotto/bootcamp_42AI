def ad(x, y):
    return x + y


def su(x, y):
    return x - y


def di(x, y):
    return x / y


def mu(x, y):
    return x * y


class Vector():
    """ Matrice """
    def __init__(self, value):
        if type(value) is tuple:
            if len(value) != 2:
                print("Error: Tupple must be a range ex (10, 15)")
                return
            x = int(value[0])
            y = int(value[1])
            self.value = range(x, y)
            self.size = len(self.value)
        if type(value) is int:
            self.value = range(value)
            self.size = len(self.value)
        if type(value) is list:
            self.value = value
        self.value = [float(i) for i in self.value]

    def __str__(self):
        strout = "Vector : "
        for i in self.value:
            strout = strout + str(i) + " - "
        return strout

    def __add__(self, num):
        try:
            num = int(num)
        except ValueError:
            print("Error, only number allowed")
            return
        v = Vector(0)
        v.value = [ad(i, num) for i in self.value]
        return v

    def __radd__(self, num):
        return self.__add__(num)

    def __sub__(self, num):
        try:
            num = int(num)
        except ValueError:
            print("Error, only number allowed")
            return
        v = Vector(0)
        v.value = [su(i, num) for i in self.value]
        return v

    def __rsub__(self, num):
        try:
            num = int(num)
        except ValueError:
            print("Error, only number allowed")
            return
        v = Vector(0)
        v.value = [su(num, i) for i in self.value]
        return v

    def __truediv__(self, num):
        try:
            num = int(num)
        except ValueError:
            print("Error")
            return
        if num == 0:
            print("You try to div by 0")
            return
        v = Vector(0)
        v.value = [di(i, num) for i in self.value]
        return v

    def __rtruediv__(self, num):
        try:
            num = int(num)
        except ValueError:
            print("Error")
            return
        if num == 0:
            print("You try to div by 0")
            return
        v = Vector(0)
        v.value = []
        for i in self.value:
            if i == 0:
                v.value.append("Error")
            else:
                v.value.append(di(num, i))
        return v

    def __mul__(self, num):
        try:
            num = int(num)
        except ValueError:
            print("Error")
            return
        v = Vector(0)
        v.value = [mu(i, num) for i in self.value]
        return v

    def __rmul__(self, num):
        return self.__mul__(num)

    def __repr__(self):
        s = str(self.value)
        return s
