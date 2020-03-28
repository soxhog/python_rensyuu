# import sys
# N = int(input())
# if N < 3 or 2 * (10**5) < N:
# 	print("error\nボールは3個以上200000以下")
# 	sys.exit()

# A = list(map(int, input().split()))
# # while not k == len(A):
# # 	# k番目の要素を除外したリストを作成
# # 	tmp = [v for i, v in enumerate(A) if not i == k]
# # 	# 何回等しくなったかflagで確認
# # 	flag = 0
# # 	j = 0
# # 	while not j == len(tmp) - 1:
# # 		h = j + 1
# # 		while not h == len(tmp):

# # 			if (tmp[j] == tmp[h]) and (not j == h):
# # 				flag += 1
# # 			h += 1
# # 		j += 1
# # 	print(flag)
# # 	k += 1
# # -----------------------------------------------------------
# # def keisan(lst, k, flag):
# # 	if k == N:
# # 		return 0
# # 	i = k + 1
# # 	flag = 0
# # 	while not i == len(lst):
# # 		if (lst[k] == lst[i]) and (not k == i):
# # 			flag += 1
# # 		i += 1
# # 	all_flag = flag + keisan(lst, k + 1, flag)
# # 	return all_flag

# # def banned_k(lst, k, all_flag):
# # 	if k == len(lst):
# # 		return 0
# # 	banned_flag = 0
# # 	i = 0
# # 	while not i == len(lst):
# # 		if (lst[k] == lst[i]) and (not k == i):
# # 			banned_flag += 1
# # 		i += 1
# # 	print(all_flag - banned_flag)
# # 	banned_k(A, k + 1, all_flag)
# # 	return 0

# # all_flag = keisan(A, 0, 0)
# # banned_k(A, 0, all_flag)

# # ----------------------------------------------------
# set_lst = [x for x in set(A)]
# nums_mutch = [0] * len(set_lst)
# i = 0
# while not i == len(set_lst):
# 	if set_lst[i] == 0:
# 		i += 1
# 		continue
# 	else:
# 		nums_mutch[i] =  A.count(set_lst[i])
# 		i += 1

# all_flag = [int((x * (x - 1)) / 2) for x  in nums_mutch]
# k = 0
# while not k == N:
# 	klist = all_flag.copy()
# 	index_k = set_lst.index(A[k])
# 	kflag = nums_mutch[index_k] - 1
# 	klist[index_k] = int((kflag * (kflag - 1)) / 2)
# 	print(sum(klist))
# 	k += 1

# --------------------------------------------------------------
N=int(input())
A=list(input().split())
check=[0]*N
for i in range(N):
	check[int(A[i])-1]+=1
num=0
# print("check =", check)
for i in range(N):
	num+=check[i]*(check[i]-1)//2
# print("num =", num)
for i in range(N):
	if check[int(A[i])-1]!=2:
		# print("i =", i, "A[i] =", A[i])
		# print("check[int(A[i])-1] - 1 =",check[int(A[i])-1] - 1)
		print(num-(check[int(A[i])-1]-1))
	else:
		print(num-1)


