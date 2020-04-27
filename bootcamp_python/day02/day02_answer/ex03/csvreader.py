class CsvReader():
    def __init__(self, filename, sep=',', header=False,
                 skip_top=0, skip_bottom=0):
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.filename = filename

    def __enter__(self):
        try:
            self.file = open(self.filename)
        except FileNotFoundError:
            print("File do not exit")
            return None
        return self

    def __exit__(self, type, value, traceback):
        self.file.close()

    def getdata(self):
        n = 0
        if self.skip_top > 0:
            for line in self.file:
                n += 1
                if self.skip_top == n:
                    break
        return self.file.read()

    def getheader(self):
        strres = ""
        n = 0
        if self.skip_top > 0:
            for line in self.file:
                n += 1
                strres = strres + line
                if self.skip_top == n:
                    break
        return strres
