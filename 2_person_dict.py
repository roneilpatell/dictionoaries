person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

# print out the name of the second child
child = person['children'][1]

print(child)




# print out the name of the cat
pet = person["pets"]['cat']

print(pet)
# use a loop to print out the names of each child
list_of_children = person["children"]
print(list_of_children)


for name in list_of_children:
    print(name)



# use a loop to print out the pets in the following format
# The type of pet is: dog and the name of the pet is: Fido
for k,v in person["pets"].items():
    print(f"the type of pet is: {k} and the name of the pet is {v}")
