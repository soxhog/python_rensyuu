import numpy

# a = numpy.array([0, 1, 2, 3])
# print(a)
# b = numpy.array([[0, 1, 2], [3, 4, 5]])
# print(b)

# print("a.shape", a.shape)
# print("b.shape", b.shape)
# print()
# print("a.size", a.size)
# print("b.size", b.size)

# print("6", numpy.arange(6))
# print("2*3", numpy.arange(6).reshape(2, 3))

# a, step = numpy.linspace(2.0, 3.0, num = 5, retstep=True)
# print(a)
# print(step)

# a = numpy.array([[1, 2], [3, 4], [5, 6], [7, 8]])
# print(a)
# print(numpy.diag(a))

# dtypeの確認
# a = numpy.arange(1, 5, dtype=float)
# print("array=", a) # 要素が少数
# print("dtype=", a.dtype)

# ao = numpy.array([[1], [2, 3]])
# print("array=", ao)
# print("dtype=", ao.dtype)

# a = numpy.array(range(4))
# print(a ** 2)

# a = numpy.array([1, 2, 3, 4])
# print(a)
# b = numpy.array([1, 2, 3, 4])
# print(b)

# print(a[0] == b[0])

# print("a[::-1] =", a[::-1])

# print("before =", a)
# a[2:] = numpy.array([10, 14])
# print("after =", a)
# b = numpy.arange(9).reshape(3, 3)
# print("b =", b)
# print()

# # aの右下2X2を取り出す
# print("b[1:, 1:] =", b[0:, 2:])

# a = numpy.arange(15)
# print("a =", a)
# mask = (a % 3 == 0)
# a[mask] = -1
# lst = list(range(0, 15, 2))
# print("index =", lst)
# print("a =", a)
# print("a[lst] =", a[lst])


# a = numpy.arange(1, 5)
# print(a)
# print()
# print("numpy.tan(a) =", numpy.tan(a))
# print("numpy.sin(a) =", numpy.sin(a))
# print("numpy.cos(a) =", numpy.cos(a))
# print()
# print("numpy.exp(a) =", numpy.exp(a))
# print()
# print("numpy.log(a) =", numpy.log(a))

# a = numpy.array([3, 1, 4, 2])
# print(a)

# print("総和", numpy.sum(a))
# print("sum", a.sum())
# print("最大値", numpy.max(a))
# print("max", a.max())
# print("最小値", numpy.min(a))
# print("平均", numpy.mean(a))
# print("中央値", numpy.median(a))
# print("分散", numpy.var(a))
# print("標準偏差", numpy.std(a))
# print("argmin =", numpy.argmin(a))
# print("argmax =", numpy.argmax(a))
# print("argmax =", a.argmax())

# b = numpy.arange(6).reshape(2, 3)
# print("b =", b)
# print("axis = 0", b.sum(axis=0))
# print("axis = 1", b.sum(axis=1))
# print("total", b.sum())
# print()
# b0 = b.sum(axis=0, keepdims=True)
# print("axis=0", b0)
# print("axis=0 shap", b0.shape)
# b1 = b.sum(axis=1, keepdims=True)
# print("axis=1", b1)
# print("axis=1 shap", b1.shape)


# ソート関数
a = numpy.array([4, 3, 1, 4, 2])
print("a", a)
print("sort", numpy.sort(a))
print("argsort", numpy.argsort(a))
mask = numpy.argsort(a)
print("a[mask]", a[mask])
