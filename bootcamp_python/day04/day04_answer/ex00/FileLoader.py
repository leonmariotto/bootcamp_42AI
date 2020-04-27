import pandas as pd


class FileLoader():
    def __init__(self):
        pass

    def load(self, path):
        try:
            data = pd.read_csv(path)
        except FileNotFoundError:
            print("File not found")
            return None
        print("Loading dataset of dimension :", data.shape)
        return(data)

    def display(self, data, n):
        if n > 0:
            print(data.head(n))
            # First n rows #
        else:
            print(data.tail(-n))
            # Last n rows #
