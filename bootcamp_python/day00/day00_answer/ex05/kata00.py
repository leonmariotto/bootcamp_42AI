import sys

t = (19, 42, 21)

print('The {:d} number are : '.format(len(t)), end='')
for i, elem in enumerate(t):
    print(elem, end='')
    if i != len(t) - 1:
        print(', ', end='')
    else:
        print('')
