# # 2倍チェック

# try:
# 	user_input = int(input())
# 	print(2 * user_input)
# except ValueError:
# 	print("error")

# -------------------------------------

# # 増件管理
# import sys
# # 何回標準入力を受け付けるか
# try:
# 	N = int(input())
# except ValueError:
# 	sys.exit()
# if N < 2 or 100000 < N:
# 	sys.exit()
# i = 0
# A = []
# while not (i == N):
# 	A.append(int(input()))
# 	if A[i] < 0 or 1000000000 < A[i]:
# 		sys.exit()
# 	i += 1

# i = 1
# while not (i == N):
# 	if A[i] == A[i - 1]:
# 		print("stay")
# 	elif A[i] < A[i - 1]:
# 		print("down", A[i - 1] - A[i])
# 	else:
# 		print("up", A[i] - A[i - 1])
# 	i += 1

# -------------------------------------

# # 三番目
# import sys

# try:
# 	input_num = list(map(int, input().split()))
# except:
# 	sys.exit()
# i = 0

# while not i == len(input_num):
# 	big_times = 0
# 	for v in input_num:
# 		if input_num[i] < v:
# 			big_times += 1
# 	if big_times == 2:
# 		break
# 	else:
# 		i += 1

# print(input_num[i])

# -------------------------------------
# #重複検査

# import sys
# import numpy

# try:
# 	times = int(input())
# except:
# 	print("error\n整数を入力")
# 	sys.exit()
# if times < 1 or 200000 < times:
# 	print("error\nNは1以上、200,000以下です")
# 	sys.exit()
# i = 0
# int_array = []
# while not i == times:
# 	try:
# 		int_array.append(int(input()))
# 	except:
# 		print("error\n整数を入力しろハゲ")
# 		sys.exit()
# 	if int_array[i] < 1 or times < int_array[i]:
# 		print(f"error\n1以上{times}以下で入力しろボケ")
# 		sys.exit()
# 	i += 1

# i = 0
# while not i == times:
# 	k = 0
# 	while not k == times:
# 		if i == k:
# 			k += 1
# 			continue
# 		if int_array[i] == int_array[k]:
# 			y = int_array[i]
# 			sum1 = numpy.sum(int_array) - y
# 			sum2 = numpy.sum(numpy.arange(times + 1))
# 			x = sum2 - sum1
# 			print(y, x)
# 			sys.exit()
# 		k += 1
# 	i += 1
# print("Correct")

# -------------------------------------
# 重複検査ver2

import sys
import numpy

try:
	times = int(input())
except:
	print("error\n整数")
	sys.exit()
if times < 1 or 200000 < times:
	print("error\n1以上、200,000以下の整数")
	sys.exit()

# times分の要素を0で埋める
lst = list(range(times + 1))
mapped_lst = list(map(lambda x: 0, lst))

i = 0
x = numpy.sum(numpy.arange(times + 1))
y = 0
while not i == times:
	input_num = int(input())
	mapped_lst[input_num] += 1
	if mapped_lst[input_num] == 2:
		y = input_num
		x += input_num
	x -= input_num
	i += 1
if y == 0:
	print("Correct")
else:
	print(y, x)
