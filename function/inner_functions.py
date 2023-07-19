def outer_function(n1, n2):
    '''
    Some dummy function
    :param n1: 1
    :param n2: 2
    :return: value is returned
    '''

    def inner_function(value):
        print(value)

    print("Outer function")
    return inner_function

outer_function(1,2)(222)


help(outer_function)

print("End")

print(outer_function.__doc__)