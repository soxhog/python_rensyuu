import random

def u_status(i):
	if i == 1:
		u_status = {'HP': 10, 'MP': 6, 'ATK': 3, 'DEF': 2, 'SPD': 2}
	elif i == 2:
		u_status = {'HP': 54, 'MP': 22, 'ATK': 18, 'DEF': 14, 'SPD': 10}
	elif i == 3:
		u_status = {'HP': 100, 'MP': 80, 'ATK': 35, 'DEF': 30, 'SPD': 25}
	elif i == 4:
		u_status = {'HP': 120, 'MP': 500, 'ATK': 70, 'DEF': 65, 'SPD': 60}
	elif i == 5:
		u_status = {'HP': 1000, 'MP': 200, 'ATK': 120, 'DEF': 400, 'SPD': 100}
	return u_status

def e_status(i):
	if i == 1:
		e_status = {'HP': 20, 'MP': 0, 'ATK': 2, 'DEF': 1, 'SPD': 1}
	elif i == 2:
		e_status = {'HP': 80, 'MP': 20, 'ATK': 20, 'DEF': 12, 'SPD': 10}
	elif i == 3:
		e_status = {'HP': 120, 'MP': 100, 'ATK': 30, 'DEF': 35, 'SPD': 28}
	elif i == 4:
		e_status = {'HP': 200, 'MP': 200, 'ATK': 200, 'DEF': 200, 'SPD': 2}
	elif i == 5:
		e_status = {'HP': 10000, 'MP': 10000, 'ATK': 3000, 'DEF': 2000, 'SPD': 2200}
	return e_status

def random_number(x):
	random_numbers = [-0.05, -0.04, -0.03, -0.02, -0.01, 0, 0.01, 0.02, 0.03, 0.04, 0.05]
	rn = random.sample(random_numbers, 1)
	x = x + x * rn[0]
	return int(x)

def show_status(status):
	print("HP:", status['HP'])
	print("MP:", status['MP'])
	print("ATK:", status['ATK'])
	print("DEF:", status['DEF'])
	print("SPD:", status['SPD'])

def line():
	print("\n--------------------------------\n")

def u_skill(skills, status):
	line()
	print("Select a skill")
	for k, v in skills.items():
		print(f"{k}		MP:{v}")
	print("\n")
	while True:
		try:
			ipt = input()
			consumption_mp = skills[ipt]
			if consumption_mp > status['MP']:
				print("\nYou don't have enough MP.\n")
				continue
			break
		except KeyError:
			print("\nSelect right skill.\n")
			continue
	line()
	return ipt

def command(status, skills):
	print("\nSelect a command")
	print("[1]Attack		[2]Guard	[3]Skill	[4]Escape")
	while True:
		try:
			c = int(input())
		except ValueError:
			print("Type right number\n")
			continue
		if c == 1 or c == 2:
			break
		elif c == 3:
			if status['MP'] >= 6:
				c = u_skill(skills, status)
				break
			else:
				print("You don't have enough MP.\n")
				continue
		elif c == 4:
			print("You can't escape from your destiny.\n")
		else:
			print("Type right number")
	return c

def e_skill(skills, status):
	for name, mp in skills.items():
		if status['MP'] < mp:
			break
		attack_skill = name
	return attack_skill

def enemy_attack(now_u_status, now_e_status):

	print("\nEnemy's attack")
	damage = random_number(now_e_status['ATK'])
	real_damage = int(damage - (now_u_status['DEF'] / 10))
	if real_damage < 0:
		real_damage = 0
	now_u_status['HP'] -= real_damage
	print("Enemy damaged", real_damage)
	return now_u_status

def enemy_action():
	action_list = [1, 1, 2]
	rn = random.sample(action_list, 1)
	action_num = rn[0]
	return action_num

def battle(i):
	u_skills = {'Slash': 6, 'Lightning': 10, 'Cure': 10, 'Super slash': 20, 'Super lightning': 30, 'Super cure': 30, 'Ultimate slash': 100, 'Ultimate lightning': 150, 'Ultimate cure': 150, 'Final break': 500}
	now_u_status = u_status(i)
	now_e_status = e_status(i)
	while now_u_status['HP'] > 0 and now_e_status['HP'] > 0:
		print("\nYour status")
		show_status(now_u_status)
		print("\nEnemy's status")
		show_status(now_e_status)
		line()
		cmd = command(now_u_status, u_skills)
		u_speed = random_number(now_u_status['SPD'])
		e_speed = random_number(now_e_status['SPD'])
		if u_speed >= e_speed:
			if cmd == 1:
				# ----------Your turn------------
				print("Your attack")
				damage = random_number(now_u_status['ATK'])
				real_damage = int(damage - now_e_status['DEF'])
				if real_damage < 0:
					real_damage = 0
				now_e_status['HP'] -= real_damage
				print("You damaged", real_damage)
				if now_e_status['HP'] <= 0:
					return 1
				# ----------enemy's turn------------
				action_num = enemy_action()
				if action_num == 1 or now_e_status['MP'] < 10:
					enemy_attack(now_u_status, now_e_status)
				elif action_num == 2 and now_e_status['MP'] >= 10:
					print("Enemy's skill")
					e_skills = {'Panch': 10, 'Kick': 50, 'Hyper beam': 100, 'Ultimate beam': 2000}
					attack_skill = e_skill(e_skills, now_e_status)
					print(attack_skill)
					damage = random_number(e_skills[attack_skill])
					real_damage = int(damage - (now_e_status['DEF'] / 10))
					if real_damage < 0:
						real_damage = 0
					now_u_status['HP'] -= real_damage
					print(f"Enemy damaged you {real_damage}")
			elif cmd == 2:
				print("Your are protectiong yourself.")
				now_u_status['DEF'] *= 2
				# ----------enemy's turn------------
				action_num = enemy_action()
				if action_num == 1 or now_e_status['MP'] < 10:
					enemy_attack(now_u_status, now_e_status)
				elif action_num == 2 and now_e_status['MP'] >= 10:
					print("Enemy's skill")
					e_skills = {'Panch': 10, 'Kick': 50, 'Hyper beam': 100, 'Ultimate beam': 2000}
					attack_skill = e_skill(e_skills, now_e_status)
					print(attack_skill)
					damage = random_number(e_skills[attack_skill])
					real_damage = int(damage - (now_e_status['DEF'] / 10))
					if real_damage < 0:
						real_damage = 0
					now_u_status['HP'] -= real_damage
					now_e_status['MP'] -= e_skills[attack_skill]
					print(f"Enemy damaged you {real_damage}")
				now_u_status['DEF'] /= 2
			else:
				# ----------Your turn------------
				print(f"Your skill		{cmd}")
				damage = random_number((now_u_status['ATK'] / 100) * u_skills[cmd] + u_skills[cmd])
				real_damage = int(damage - (now_e_status['DEF'] / 10))
				if real_damage < 0:
					real_damage = 0
				now_e_status['HP'] -= real_damage
				now_u_status['MP'] -= u_skills[cmd]
				print("You damaged", real_damage)
				if now_e_status['HP'] <= 0:
					return 1
				# ----------enemy's turn------------
				action_num = enemy_action()
				if action_num == 1 or now_e_status['MP'] < 10:
					enemy_attack(now_u_status, now_e_status)
				elif action_num == 2 and now_e_status['MP'] >= 10:
					print("Enemy's skill")
					e_skills = {'Panch': 10, 'Kick': 50, 'Hyper beam': 100, 'Ultimate beam': 2000}
					attack_skill = e_skill(e_skills, now_e_status)
					print(attack_skill)
					damage = random_number(e_skills[attack_skill])
					real_damage = int(damage - (now_e_status['DEF'] / 10))
					if real_damage < 0:
						real_damage = 0
					now_u_status['HP'] -= real_damage
					now_e_status['MP'] -= e_skills[attack_skill]
					print(f"Enemy damaged you {real_damage}")
		elif u_speed < e_speed:
			# ----------enemy's turn------------
			tmp = now_u_status['DEF']
			if cmd == 2:
				print("Your are protectiong yourself.")
				now_u_status['DEF'] *= 2
			action_num = enemy_action()
			if action_num == 1 or now_e_status['MP'] < 10:
				enemy_attack(now_u_status, now_e_status)
			elif action_num == 2 and now_e_status['MP'] >= 10:
				print("Enemy's skill")
				e_skills = {'Panch': 10, 'Kick': 50, 'Hyper beam': 100, 'Ultimate beam': 2000}
				attack_skill = e_skill(e_skills, now_e_status)
				print(attack_skill)
				damage = random_number(e_skills[attack_skill])
				real_damage = int(damage - (now_e_status['DEF'] / 10))
				if real_damage < 0:
					real_damage = 0
				now_u_status['HP'] -= real_damage
				now_e_status['MP'] -= e_skills[attack_skill]
				print(f"Enemy damaged you {real_damage}")
			if not tmp == now_u_status['DEF']:
				now_u_status['DEF'] /= 2
			if now_u_status['HP'] <= 0:
				return 0
			# ----------Your turn------------
			if cmd == 1:
				print("Your attack")
				damage = random_number(now_u_status['ATK'])
				real_damage = int(damage - (now_e_status['DEF'] / 10))
				if real_damage < 0:
					real_damage = 0
				now_e_status['HP'] -= real_damage
				print("You damaged", real_damage)
			else:
				print(f"Your skill		{cmd}")
				damage = random_number((now_u_status['ATK'] / 100) * u_skills[cmd] + u_skills[cmd])
				real_damage = int(damage - (now_e_status['DEF'] / 10))
				if real_damage < 0:
					real_damage = 0
				now_e_status['HP'] -= real_damage
				now_u_status['MP'] -= u_skills[cmd]
				print("You damaged", real_damage)
	if now_e_status['HP'] <= 0:
		return 1
	else:
		return 0

i = {'1', '2', '3', '4', '5'}
for v in i:
	i = int(v)
	break
if battle(i) == 1:
	print("\nYOU WIN!!!!")
else:
	print("\nYOU LOSE")
