while 1:
	print ("\n整数xを入力してください。")
	try:
		x = int(input("x = "))
	except ValueError:
		print("\nError")
		continue
	break
if x < 0:
	print('xは負の整数です')
elif x > 0:
	print('xは正の整数です')
else:
	print('xは0です')
