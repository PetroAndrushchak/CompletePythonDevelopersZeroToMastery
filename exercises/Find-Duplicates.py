some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []

for index, element in enumerate(some_list):
    for j in range(index + 1, len(some_list)):
        if element == some_list[j]:
            duplicates.append(element)
            # print(f'{index} {j}')

print(duplicates)

duplicates_2 = []
for element in some_list:
    if some_list.count(element) > 1 and element not in duplicates_2:
        duplicates_2.append(element)

print(duplicates_2)
