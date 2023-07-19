for item in "Petro":
    print(item)

for item in [1, 2, 4, 5, 6]:
    print(item)

for item in (1, 2, 34, 5, 6):
    print(item)

for item in {1, 3, 4, 5, 6, 7}:
    print(item)

for i in [1, 2, 3, 4, 5]:
    for j in [1, 2, 3, 4, 5, 6, 7]:
        print(str(i) + " and " + str(j))

user = {
    'name': 'Petro',
    'age': 20
}

for item in user:
    print(item)

for item in user.items():
    print(item)

for item in user.keys():
    print(item)

for item in user.values():
    print(item)

print("Key and Value")

for key, value in user.items():
    print(key + ' and ' + str(value))