# usage: python3 headers_collecting_arguments.py

# NOTE: positional arguments cannot follow keyword arguments!!!

def ft(*args):
    # NOTE: an function parameter prefixed by a star collects unmatched
    # positional arguments passed to it into a tuple
    print(args)


def fd(**args):
    # NOTE: an function parameter prefixed by two stars collects unmatched
    # positional arguments passed to it into a dictionary
    print(args)


def ftd(a, *pargs, **kargs):
    # NOTE: when defining a function with * and ** parameters, the * parameter
    # must appear before the ** parameter
    print(a, pargs, kargs)


if __name__ == '__main__':
    print('code snippets from page 555\n')

    # NOTE: if no argument is passed to a function that defines a * parameter,
    # the call instantiates an empty tuple in its place
    ft()  # ()
    ft(1)  # (1,)
    ft(1, 2, 3, 4)  # (1,2,3,4)
    print('')

    # NOTE: if no argument is passed to a function that defines a ** parameter,
    # the call instantiates an empty dictionary in its place
    fd()  # {}
    fd(a=1, b=2)  # {'a':1,'b':2}

    try:
        # fd() requires arguments and will not accept positional
        # arguments
        fd([1, 2])
    except TypeError as ex:
        print(ex)
    print('')

    # a receives 1, pargs receives 2 and 3, and kargs receives x and y
    ftd(1, 2, 3, x=1, y=2)  # 1 (2, 3), {'x':1, 'y':2}
