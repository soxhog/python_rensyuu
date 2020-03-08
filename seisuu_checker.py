while 1:
	print ("\ninput integer x")
	try:
		x = int(input("x = "))
	except ValueError:
		print("\nError")
		continue
	break
if x < 0:
	print('x is negative integer')
elif x > 0:
	print('x is positive integer')
else:
	print('x is 0')
