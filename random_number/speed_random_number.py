random_number = {'-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'}
u_speed = int(input("Your speed is "))
e_speed = int(input("Enemy's speed is "))
print()
for rn in random_number:
	u_speed = u_speed + int(rn)
	print("Your speed + ramdom number is", u_speed)
	break
print()
for rn in random_number:
	e_speed = e_speed + int(rn)
	print("Enempy's speed + ramdom number is", e_speed)
	break
print()

if u_speed > e_speed:
	print("You are faster than enemy.")
elif u_speed < e_speed:
	print("You are slower than enemy.")
else:
	print("You and enemy are the same speed")
