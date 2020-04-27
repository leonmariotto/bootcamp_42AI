from matrix import Matrix
from vector import Vector

print("Matrix with list")
print(Matrix([[1,2,3],[4,5,6]]))

print("Matrix with tuple")
print(Matrix((3,3)))


m = Matrix([[1,2,3],[4,5,6]])
n = Matrix([[5,8,9],[4,5,6]])
o = Matrix([[5,8],[4,5],[2,3]])
v = Vector(3)

print("Matrix + Scalar")
print(m + 2)
print("Matrix - Scalar")
print(m - 2)
print("Scalar - Matrix")
print(2 - m)
print("Matrix + Matrix")
print(m + n)
print("Matrix - Matrix")
print(m - n)
print("Reversed Matrix - Matrix")
print(n - m)

print("Matrix / Scalar")
print(m / 2)
print("Matrix / Scalar")
print(m / 2)

print("Matrix * Scalar")
print(m * 3)
print("Matrix * Vector")
print(m * v)
print("Matrix * Matrix")
print(m * o)
