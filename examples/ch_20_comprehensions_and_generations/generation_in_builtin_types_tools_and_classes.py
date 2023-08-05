# usage: python3 generation_in_builtin_types_tools_and_classes.py

# function prints its arguments
def f(a, b, c):
    print('%s, %s, and %s' % (a, b, c))


if __name__ == '__main__':
    print('code snippets from pages 629-631\n')

    D = {'a': 1, 'b': 2, 'c': 3}
    print(D)  # {'a':1,'b':2,'c':3}
    # NOTE: dictionaries are iterables with iterators that produce keys on each
    # iteration
    x = iter(D)
    print(next(x))  # a
    print(next(x))  # b
    print(D[next(x)])  # 3
    print('')

    for key in D:
        print(key, D[key])  # a 1, b 2, c 3
    print('')

    f(0, 1, 2)  # 0 1 2... positional arguments
    f(*range(3))  # 0 1 2... unpack range iterable in 3X
    f(*(i for i in range(3)))  # 0 1 2... unpack generator expression
    print('')

    D = dict(a='Bob', b='dev', c=40.5)
    print(D)  # {'a':'Bob', 'b':'dev', 'c':40.5}
    f(a='Bob', b='dev', c=40.5)  # Bob dev 40.5... normal keyword arguments
    f(**D)  # Bob dev 40.5... unpack values from dictionary
    f(*D)  # a b c... unpack keys
    f(*D.values())  # Bob dev 40.5... unpack values
    print('')

    for x in 'spam':
        print(x.upper(), end=' ')  # s p a m
    print('')

    # coerce processing of generator expression using list comprehension
    list(print(x.upper(), end=' ') for x in 'spam')  # SPAM
    print('')

    # same
    [print(x.upper(), end=' ') for x in 'spam']  # SPAM
    print('')

    # coerce processing of generator expressing using dictionary comprehension
    {print(x.upper(), end=' ') for x in 'spam'}  # SPAM
    print('')

    # unpack results of generator expression to provide arguments to print()
    print(*(x.upper() for x in 'spam'))  # SPAM
    
    # coerce processing of generator expression with a generator expression
    (print(x.upper(), end=' ') for x in 'spam')

