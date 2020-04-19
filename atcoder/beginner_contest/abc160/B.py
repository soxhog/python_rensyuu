# Golden Coins
X = int(input())
num500 = X // 500
num5 = (X - num500 * 500) // 5
print(num500 * 1000 + num5 * 5)
