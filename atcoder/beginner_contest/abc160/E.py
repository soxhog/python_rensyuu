# Red and Green Apples

first_line = list(map(int, input().split()))
X, Y, A, B, C = first_line[0], first_line[1], first_line[2], first_line[3], first_line[4]
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
print(p)
print(q)
print(r)
yum = 0

def keisan(yum):
	return yum

while X != 0 and Y != 0:
	pmax = 0
	qmax = 0
	rmax = 0
	if 0 < A:
		pmax = max(p)
	if 0 < B:
		qmax = max(q)
	if 0 < C:
		rmax = max(r)
	if rmax - pmax > 0 or rmax - qmax > 0:
		print(rmax)
	else:
		print("else")
