import numpy

A = numpy.array([[1, 3], [5, 7]])
B = numpy.array([[2, 4], [6, 8]])

print("A =\n", A)
print()
print("B =\n", B)
print()
# print("A + B =\n", A + B)
# print()
# print("A - B =\n", A - B)

# # 要素積
# print()
# print("3A=\n", 3 * A)
# print()
# print("A * B =\n", A * B)

# # 行列の積
# print()
# print("A × B =\n", A.dot(B))
# print()
# print("B × A =\n", B.dot(A))

# 転置
print()
print("A転置 =", A.T)
# Aの転置の転置は
print(numpy.array_equal(A.T.T, A))
