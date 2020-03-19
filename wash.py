import re

# shortcut list
space = "\n-------------------------------------\n"

# ----------------main------------------------------

usr_input_word = input("please input word --> ")

def wash_word(usr_input_word):
    is_target = {'stupid':'', 'fuck':'', 'poor':'', 'tomo':'I can not wash. cuz He is very good man', 'kagiya':'All dirt is gone'}
    return re.sub( '({})'.format('|'.join(map(re.escape, is_target.keys()))), lambda m: is_target[m.group()], usr_input_word)

print(space)
print(wash_word(usr_input_word))
print(space)
