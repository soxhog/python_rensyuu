NK = list(map(int, input().split()))
N = NK[0]
K = NK[1]

i = 0
lst = [0] * (N + 1)
while i < N + 1:
	lst[i] = i
	i += 1
print(lst)
