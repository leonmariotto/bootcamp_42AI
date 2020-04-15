import time
import os


def ft_progress(listy):
    count = len(listy)
    begin = time.time()
    litime = []
    def show(j):
        x = int(40 * j/count)
        now = time.time()
        moytime = 0
        for i in litime:
            moytime += i
        moytime /= len(litime)
        print("ETA : {:2.2f}s [{:2d}%][{:s}{:s}] {:d}/{:d} | elapsed time\
 {:2.2f}s".format((count - j) * moytime, int(100*j/count),
 "#"*x, "."*(40-x), j, count, now - begin), end='\r')
    for i, item in enumerate(listy):
        pre = time.time()
        yield item
        aft = time.time()
        litime.append(aft - pre)
        show(i + 1)


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)
