class TinyStatistician():
    def __init__(self):
        pass

    def mean(self, x):
        if x == []:
            return None
        m = 0
        for i in x:
            m += i
        m /= len(x)
        return m

    def median(self, x):
        if x == []:
            return None
        n = sorted(x)
        return n[int(len(x) / 2)]

    def quartiles(self, x, percentile):
        if x == []:
            return None
        n = sorted(x)
        return float(n[int(len(x) * (percentile / 100))])

    def var(self, x):
        if x == []:
            return None
        v = 0
        u = self.mean(x)
        for i in x:
            v += (i - u) ** 2
        v /= len(x)
        return v

    def std(self, x):
        return self.var(x) ** 0.5
