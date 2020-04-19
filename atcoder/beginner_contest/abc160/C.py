# Traveling Salesman around Lake
S = list(map(int, input().split()))
K, N= S[0], S[1]
A = list(map(int, input().split()))

# それぞれの家の間隔リストを作る
kankaku = [0] * N

for i, v in enumerate(A):
	if i == 0:
		# 最後の家との距離
		kankaku[i] = A[i] + (K - A[N - 1])
	else:
		kankaku[i] = v - A[i - 1]

kankaku.remove(max(kankaku))
print(sum(kankaku))
