names = {
    'name_1': "Petro",
    'name_2': "Pavlo",
}

print(names)


user = dict(name='Petro')

print(user)


print('name_1' in names)
print('Petro' in names.items())


print(names.popitem())
print(names.pop('name_1'))