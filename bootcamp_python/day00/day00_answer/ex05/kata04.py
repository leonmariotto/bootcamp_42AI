t = (0, 4, 132.422222, 10000, 12345.67)

print('day_', "{:02d}".format(t[0]), sep='', end=', ')
print('ex_', "{:02d}".format(t[1]), sep='', end=' : ')
print("{:.2f}".format(t[2]), end=', ')
print("{:.2e}".format(t[3]), end=', ')
print("{:.2e}".format(t[4]))
