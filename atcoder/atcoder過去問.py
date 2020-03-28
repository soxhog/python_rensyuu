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
# # 重複検査ver2

# import sys
# import numpy

# try:
# 	times = int(input())
# except:
# 	print("error\n整数")
# 	sys.exit()
# if times < 1 or 200000 < times:
# 	print("error\n1以上、200,000以下の整数")
# 	sys.exit()

# # times分の要素を0で埋める
# lst = list(range(times + 1))
# mapped_lst = list(map(lambda x: 0, lst))

# i = 0
# x = numpy.sum(numpy.arange(times + 1))
# y = 0
# while not i == times:
# 	input_num = int(input())
# 	mapped_lst[input_num] += 1
# 	if mapped_lst[input_num] == 2:
# 		y = input_num
# 		x += input_num
# 	x -= input_num
# 	i += 1
# if y == 0:
# 	print("Correct")
# else:
# 	print(y, x)

# -------------------------------------

# # SNSのログ

# import sys

# def follow(log, users):
# 	user = log[1] - 1
# 	followed_user = log[2] -1
# 	users[user][followed_user] = True
# 	return users

# def followall(log, users):
# 	user = log[1] - 1
# 	i = 0
# 	while not len(users) == i:
# 		if (users[i][user] == True) and (not user == i):
# 			users[user][i] = True
# 		i += 1
# 	return users

# def followfollow(log, users, user_num):
# 	user = log[1] - 1
# 	i = 0
# 	current_follow = users[user].copy()
# 	for v in current_follow:
# 		if (v == True) and (not i == user):
# 			h = 0
# 			for k in users[i]:
# 				if (k == True) and (not h == user) and (not h == i):
# 					users[user][h] = True
# 				h += 1
# 		i += 1
# 	return users

# def first_error_check(tmp, user_num, log_num):
# 	if not len(tmp) == 2:
# 		print("error\nuser数と操作ログのみを最初の行に入力")
# 		sys.exit()
# 	if user_num < 2 or 100 < user_num:
# 		print("error\nuser数は2以上、100以下")
# 		sys.exit()
# 	elif log_num < 0 or 500 < log_num:
# 		print("error\n行は0以上、500以下")
# 		sys.exit()
# 	return

# try:
# 	# user数と操作ログ数を取得
# 	tmp = list(map(int, input().split()))
# 	user_num = tmp[0]
# 	log_num = tmp[1]
# 	# userのログを取得
# 	logs = [list(map(int, input().split())) for _ in range(log_num)]
# except:
# 	print("error\n整数を入力")
# 	sys.exit()
# # errorチェック
# first_error_check(tmp, user_num, log_num)

# # users = [[False for i in range(user_num)] for j in range(user_num)]
# #　上のでもいいけどよりシンプルな内包表記が下の
# users = [[False] * user_num for _ in range(user_num)]
# i = 0
# while not log_num == i:
# 	if logs[i][0] == 1:
# 		users = follow(logs[i], users)
# 	elif logs[i][0] == 2:
# 		users = followall(logs[i], users)
# 	else: # logs[i][0] == 3:
# 		users = followfollow(logs[i], users, user_num)
# 	# else:
# 	# 	print(f"error\n{i + 2}行目のログ操作の一番最初の数字は1~3の間")
# 	# 	sys.exit()
# 	i += 1

# for v in users:
# 	follow_status = []
# 	followed_user = 0
# 	while not followed_user == user_num:
# 		if v[followed_user] == True:
# 			follow_status.append("Y")
# 		else:
# 			follow_status.append("N")
# 		followed_user += 1
# 	print("".join(follow_status))

# -------------------------------------

# DoubleCamelCase Sort

# user_input = input()
# split_lst = []
# i = 0
# tmp = ""
# # flagで何回大文字が出たか確認する
# flag = 0
# while True:
# 	if i == len(user_input):
# 		break
# 	tmp += user_input[i]
# 	# .isupper()で大文字かどうか判断
# 	# if "A" <= user_input[i] and user_input[i] <= "Z": ## これでもOK
# 	if user_input[i].isupper():
# 		flag += 1
# 	if flag == 2:
# 		split_lst.append(tmp)
# 		tmp = ""
# 		flag = 0
# 	i += 1
# copy_splist = split_lst.copy()
# memory_lst = []
# i = 0
# for v in copy_splist:
# 	tmp = [v, v.upper()]
# 	copy_splist[i] = v.upper()
# 	memory_lst.append(tmp)
# 	i += 1

# sort_lst = sorted(copy_splist)
# j = 0
# for v in sort_lst:
# 	i = 0
# 	while True:
# 		if memory_lst[i][1] == v:
# 			sort_lst[j] = memory_lst[i][0]
# 			j += 1
# 			break
# 		i += 1
# print("".join(sort_lst))

# -------------------------------------

# DoubleCamelCase Sort version 2

# user_input = input()
# split_lst = []
# i = 0
# tmp = ""
# # flagで何回大文字が出たか確認する
# flag = 0
# while True:
# 	if i == len(user_input):
# 		break
# 	tmp += user_input[i]
# 	# .isupper()で大文字かどうか判断
# 	# if "A" <= user_input[i] and user_input[i] <= "Z": ## これでもOK
# 	if user_input[i].isupper():
# 		flag += 1
# 	if flag == 2:
# 		split_lst.append(tmp)
# 		tmp = ""
# 		flag = 0
# 	i += 1

# # 全て小文字にする
# lower_lst = [v.lower() for v in split_lst]
# # ソート
# sort_lst = sorted(lower_lst)
# # それぞれの要素の最初の文字と最後の文字を大文字にする
# i = 0
# while not i == len(sort_lst):
# 	j = 0
# 	letter = ""
# 	while not j == len(sort_lst[i]):
# 		#最初の文字を大文字
# 		if j == 0:
# 			letter += sort_lst[i][j].upper()
# 			j += 1
# 			continue
# 		#最後の文字を大文字
# 		elif j == len(sort_lst[i]) - 1:
# 			letter += sort_lst[i][j].upper()
# 			j += 1
# 			continue
# 		else:
# 			letter += sort_lst[i][j]
# 			j += 1
# 	# 最初と最後の文字を大文字にした文字列を入れ直す
# 	sort_lst[i] = letter
# 	i += 1
# print("".join(sort_lst))

# -------------------------------------

# G 組み分け

import sys

# 人数を受け取る
try:
	# グローバル変数
	member_num = int(input())
except:
	print("整数を入力")
	sys.exit()
if member_num < 2 or 10 < member_num:
	print("人数は2人以上10人以下")
	sys.exit()

# ペアの幸福値を取得
# グローバル変数
happy_pair_lst = [list(map(int, input().split())) for _ in range(member_num - 1)]
print(happy_pair_lst)


