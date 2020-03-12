numbers = [i for i in range(10)]
print(numbers)

#-------------<close()を使う方法>------------------
# f = open("numbers.txt", "w")
# for number in numbers:
# 	f.write(f"{number},{number ** 2}\n")
# print(f.closed)
# f.close()
# print(f.closed)

#-------------<close()を使わない方法>------------------
with open("numbers.txt", "w") as f:
	for number in numbers:
		f.write(f"{number}, {number ** 2}\n")


# -----------------print("#readlines")--------------------
# with open("numbers.txt", "r") as f:
# 	# 全行読み込み
# 	lines = f.readlines()
# print("f.readlines() =", lines)
# for line in lines:
# 	print(line, end="")

# -----------------print("# readline")---------------------
# with open("numbers.txt", "r") as f:
# 	# ファイルの終わりまでreadlineを繰り返す
# 	while True:
# 		line = f.readline()
# 		if line == "":
# 			break
# 		print(line, end="")

# より効率的な方法
with open("numbers.txt", "r") as f:
	for line in f:
		line = line.rstrip()
		splited = line.split(",")
		number = [int(i) for i in splited]
		print(f"{number[0]} + {number[1]} = {number[0] + number[1]}")
