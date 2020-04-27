from TinyStatistician import *

t = TinyStatistician()
a = [1, 42, 300, 10, 59]

print("mean")
print(t.mean(a))
print("median")
print(t.median(a))
print("quartil")
print(t.quartiles(a, 75))
print("var")
print(t.var(a))
print("std")
print(t.std(a))

