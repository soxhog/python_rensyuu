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
