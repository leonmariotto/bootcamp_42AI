import numpy as np
import sys

def unique(lst):
    ulst = []
    for m in lst:
        if m not in ulst:
            ulst.append(m)
    return ulst
        
def generator(text, sep=" ", option=None):
    try:
        lst = text.split(sep)
    except NameError:
        print("Error")
        return
    if option == 'shuffle':
        np.random.shuffle(lst)
    elif option == 'ordered':
        lst.sort()
    elif option == 'unique':
        lst = unique(lst)
    elif option is not None:
        print("Error, option not valid, exit")
        sys.exit()
    for word in lst:
        yield word
