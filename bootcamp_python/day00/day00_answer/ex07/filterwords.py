import sys

if len(sys.argv) != 3:
    print("ERROR")
    sys.exit()

try:
    x = int(sys.argv[2])
    s = sys.argv[1].replace(',', '')
    s = s.replace('.', '')
    lst = s.split(' ')
except ValueError:
    print("ERROR")
    sys.exit()

reslst = []
for word in lst:
    if len(word) > x:
        reslst.append(word)

print(reslst)
