# -------------------< old >-------------------------

# random_number = {'-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'}
# u_speed = int(input("Your speed is "))
# e_speed = int(input("Enemy's speed is "))

# print()
# for rn in random_number:
# 	u_speed = u_speed + int(rn)
# 	print("Your speed + ramdom number is", u_speed)
# 	break
# print()
# for rn in random_number:
# 	e_speed = e_speed + int(rn)
# 	print("Enempy's speed + ramdom number is", e_speed)
# 	break
# print()

# -------------------< end >-------------------------

# -------------------< what I've wanted to code >-------------------------

random_number = {'-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'}
u_speed = int(input("Your speed is "))
e_speed = int(input("Enemy's speed is "))

print("\n")
for i, rn in enumerate(random_number):
	if i == 0:
		u_speed = u_speed + int(rn)
		print("Your speed + ramdom number is", u_speed)
	elif i == 1:
		e_speed = e_speed + int(rn)
		print("\n")
		print("Enempy's speed + ramdom number is", e_speed)
		break
print("\n")

# -------------------< end >-------------------------

# -------------------< giving up new one >-------------------------
# import random

# random_numbers = list(range(-5, 6))
# u_rn = random.sample(random_numbers, 1)
# e_rn = random.sample(random_numbers, 1)
# u_speed = int(input("Your speed is "))
# e_speed = int(input("Enemy's speed is "))

# print("\n")
# u_speed = u_speed + u_rn[0]
# print("Your speed + ramdom number is", u_speed)
# print("\n")
# e_speed = e_speed + e_rn[0]
# print("Enempy's speed + ramdom number is", e_speed)
# print("\n")

# -------------------< end >-------------------------

# -------------------< 線形合同法 >-------------------------
# u_speed = int(input("Your speed is "))
# e_speed = int(input("Enemy's speed is "))

# u_random_number = id(3.0) * id(5.0) % 37
# u_random_number = (11 * u_random_number + 3) % 10
# e_random_number = id(7.0) * id(5.0) % 37
# e_random_number = (11 * e_random_number + 3) % 10

# print("\n")
# u_speed = u_speed + u_random_number
# print("Your speed + ramdom number is", u_speed)
# print("\n")
# e_speed = e_speed + e_random_number
# print("Enempy's speed + ramdom number is", e_speed)
# print("\n")
# -------------------< end >-------------------------
if u_speed > e_speed:
	print("You are faster than enemy.")
elif u_speed < e_speed:
	print("You are slower than enemy.")
else:
	print("You and enemy are the same speed")
