import sys

try:
	nums = list(map(int, input().split()))
	N, M = nums[0], nums[1]
except:
	print("整数を入力")
	sys.exit()

if (N < 0 or 100 < N) or (M < 0 or 100 < M):
	print("NとMはそれぞれ0以上100以下")
	sys.exit()
if N + M < 2:
	print("N + Mは2以上")
	sys.exit()

# ------------------------------------------------------
# def keisan(num):
# 	# 組み合わせの数をcntでカウント
# 	cnt = 0
# 	while not num == 0:
# 		copy_num = num
# 		while not (copy_num - 1) == 0:
# 			copy_num -= 1
# 			cnt += 1
# 		num -= 1
# 	return cnt

# sum = keisan(N) + keisan(M)
# print(sum)
# ------------------------------------------------------

# 上の点線の中身は下の2行でできるみたい。。。。。。。つらっ
sum = int((N * (N - 1)) / 2) + int((M * (M - 1)) / 2)
print (sum)
