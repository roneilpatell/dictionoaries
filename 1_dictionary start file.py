import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}


'''
print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(len(phonebook))

mydictionary = {}
mydictionary = dict(m=8,n=9)

print(mydictionary)

phone = phonebook['Chris']
[print(phone)]



print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'Chris'
if name in phonebook:
    print(phonebook[name])
else:
    print(f"{name} is not in phonebook")






print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()



print(phonebook)
phonebook["Joe"] = '555-0123'
phonebook['Chris'] = '555-444'

print(phonebook)

print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

print(phonebook)
del phonebook['Chris']

print(phonebook)




print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for key in phonebook:
    print(f"the key is {key} and the value is {phonebook[key]}")

for v in phonebook.values():
    print(v)

for item in phonebook.items():
    print(item)

for k,v in phonebook.items():
    print(f"the key is {k} and the value is {v}")



print()
print('*****  end section 5 ********')
print()







print()
print('*****  start section 6 - using get and clear ********')
print()

print(phonebook)
phone = phonebook.get('chris', 'Not found')

print(phone)


phonebook.clear()

print(phonebook)






print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()


phone = phonebook.pop('Chris', 'not found')

print(phone)
print(phonebook)




print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()

keyvalue= phonebook.popitem()

print(phonebook)



print()
print('*****  end section 8 ********')
print()

'''

print()
print('*****  start section 9 - using random and converting to list ********')
print()

list_of_keys = list(phonebook)
randomkey = random.choice(list_of_keys)
print(randomkey)
print(phonebook[randomkey])

print(phonebook[random.choice(list(phonebook))])



print()
print('*****  end section 9 ********')
print()








