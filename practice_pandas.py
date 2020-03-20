import numpy
import pandas

numpy.random.seed(42)

# 10行5列の配列（要素は乱数）を作る
data = numpy.random.randn(10, 5)
# print(data)

df = pandas.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'])
# print(df.head(3))
# print(df.tail(3))

# print(df.index)
# print()
# print(df.columns)
# print()
# print(df)

# print(df.values)

# print(df.describe())

# 一つだけのカラムを取得
# print('B')

# 2行目から5行目を取得
# print(df[1:5])

#行とカラム両方を指定
# print(df.loc[1:3, ['A', 'C', 'E']])

# # ilocプロパティは行と列の位置を指定して選択
# print(df)
# print()
# # 4行目
# print(df.iloc[3])
# # 2から3行目、2から3列目
# print(df.iloc[1:3, 0:2])

# # mask = (df['A'] >= 0)
# mask = (df >= 0)
# print(mask)
# print()
# print(df[mask])

# print(df)
# print()
# print(df.mean(axis=1))
# print((df.sum(axis=1) / 5))


import matplotlib
from matplotlib import pyplot
print(df.plot(figsize=(11, 7), title='Test Plot', legend=True))
df.show()
