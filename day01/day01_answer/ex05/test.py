from bank import Account, Bank

b = Bank()
a = Account("Jb", zip="zipped")
a.value = 100
b.add(a)

a = Account("Jm", zip="zipped")
a.value = 100
b.add(a)

print(b.account[0])
print(b.account[1])
b.transfer("Jb", "Jm", 30)
print(b.account[0])
print(b.account[1])

b.fix_account("Jb")
b.fix_account("Jm")
print(b.account[0])
print(b.account[1])
b.transfer("Jb", "Jm", 30)
print(b.account[0])
print(b.account[1])
