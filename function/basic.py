def say_hello():
    print("Helloooo")


say_hello()

# positional arguments

# parameters
def say_hello_two(name='Pavlo', word='Hi'):
    print(f'Hello {name} with word: {word}')


# arguments
say_hello_two('Petro', "Happy")

# keywords arguments

say_hello_two(word='Happy', name='Andrii')
say_hello_two()
