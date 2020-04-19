N = int(input())
A = list(map(int, input().split()))
lst = [0] * N
for i in A:
	lst[i - 1] += 1
for k in lst:
	print(k)
