# usage: python3 calls_unpacking_arguments.py

# function outputs its arguments
def func(a, b, c, d):
    print(a, b, c, d)


if __name__ == '__main__':
    print('code snippets from page 556\n')

    args = (1, 2)
    args += (3, 4)
    print(args)  # (1,2,3,4)

    # NOTE: when an argument passed to a function is prefixed with a *, it is
    # unpacked as a tuple/positional argument
    func(*args)  # 1 2 3 4.. same as func(1,2,3,4)
    print('')

    args = {'a': 1, 'b': 2, 'c': 3}
    args['d'] = 4
    print(args)  # {'a':1,'b':2,'c':3,'d':4}

    # NOTE: when an argument passed to a function is prefixed with **, it is
    # unpaced as a dictionary/keyword argument
    func(**args)  # 1 2 3 4... same as func(a=1,b=2,c=3,d=4)
    print('')

    # NOTE: iterable arguments must come before keyword arguments
    func(*(1, 2), **{'d': 4, 'c': 3})  # 1 2 3 4... same as func(1,2,d=4,c=3)
    
    func(1, *(2, 3), **{'d': 4})  # 1 2 3 4... same as func(1,2,3,d=4)

    # NOTE: here *(2,) is unpacked as a tuple and assigned to the remaining
    # positional argument... in this case b. in order for this to work, the
    # value after the * must be iterable since *(2) unpacks to an int
    func(1, c=3, *(2,), **{'d': 4})  # 1 2 3 4... same as func(1,2,c=3,d=4)

    # NOTE: here *([2]) is ok since a list is iterable and can be unpacked as a
    # tuple
    func(1, c=3, *([2]), **{'d': 4})  # 1 2 3 4... same as func(1,2,c=3,d=4)
    
    # NOTE: here, since [2] is iterable, it is not necessary to surround it
    # with parentheses for it to be unpacked correctly
    func(1, c=3, *[2], **{'d': 4})  # 1 2 3 4, func(1,2,c=3,d=4)
    
    func(1, *(2, 3), d=4)  # 1 2 3 4... same as func(1,2,3,d=4)

    func(1, *(2,), c=3, **{'d': 4})  # 1 2 3 4... same as func(1,2,c=3,d=4)
