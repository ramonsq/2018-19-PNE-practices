import json
import termcolor

f = open("personex1.json", "r")

people = json.load(f)

print()
print("Total people in the database: ", len(people))
print()
for person in people:
    termcolor.cprint("Name: ", "green", end='')
    print(person['Firstname'], person['Lastname'])
    termcolor.cprint("Age: ", "green", end='')
    print(person['age'])
    termcolor.cprint("Phone numbers: ", "green", end='')
    print(len(person['phoneNumber']))
    for i, num in enumerate(person['phoneNumber']):
        termcolor.cprint("  Phone {}".format(i+1), end='\n')

        termcolor.cprint("    Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("    Number: ", 'red', end='')
        print(num['number'])
