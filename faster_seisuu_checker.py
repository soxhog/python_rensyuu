def num_checker():
	try:
		n = int(input("n = "))
	except ValueError:
		print("\nError\n")
		print("input right integer")
		return num_checker()
	if n < 0:
		print('n is negative integer')
	elif n > 0:
		print('n is positive integer')
	else:
		print("n is 0")

print("input number")
num_checker()
