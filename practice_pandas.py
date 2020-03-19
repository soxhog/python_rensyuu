import numpy
import pandas

numpy.random.seed(42)

# 10行5列の配列（要素は乱数）を作る
data = numpy.random.randn(10, 5)
print(data)

df = pandas.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'])
print(df)
