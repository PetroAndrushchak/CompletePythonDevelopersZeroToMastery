basket = ['x', 'a', 'b', 'c', 'd']

print(basket.index('c'))

print('a' in basket)

print(basket.count('a'))

basket.sort()
print(basket)

new_basket = sorted(basket)
print(new_basket)

basket.reverse()
print(basket)

joiner = ' '
new_string = joiner.join(['hi', 'my', 'name', 'is', 'Petro'])
print(new_string)

second_string = joiner.join("petro")
print(second_string)

