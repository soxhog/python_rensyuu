def gattai(s):
	g = ""
	for j in s:
		g += j
	return g

def judge(S, N):
	# 真ん中より左 list型なのでgattaiさせる
	S1 = gattai(S[:int(N / 2)])
	# 真ん中より右
	S2 = gattai(S[int(N / 2 + 1):])
	if S1 == S2:
		if S1 == S1:
			if S2 == S2:
				return "Yes"
	return "No"

S = list(input())
N = len(S)
print(judge(S, N))
