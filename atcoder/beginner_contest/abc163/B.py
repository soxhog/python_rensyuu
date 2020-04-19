NM = list(map(int, input().split()))
N = NM[0]
M = NM[1]
A = list(map(int, input().split()))
if N < M:
	print(-1)
sum = 0
for i in A:
	sum += i
if N - sum < 0:
	print(-1)
else:
	print(N - sum)
