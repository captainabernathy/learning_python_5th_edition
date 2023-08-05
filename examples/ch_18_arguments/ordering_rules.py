# usage: python3 ordering_rules.py

# NOTE: if a function includes a ** parameter, it must be defined last in the
# header, and when that function is called, the argument provided to a **
# paramter must be provided last... or not at all

# NOTE: if a function includes both a ** paramter and a keyword-only parameter
# the keyword-only paramter may receive its argument from a key-value pair of
# the same name that has been packed into the ** argument by the caller

# a is a positional argument, b collects arbitrary positional arguments,
# c is a keyword-only argument, and d collects arbitrary keyword arguments
def f1(a, *b, c=6, **d):
    print(a, b, c, d)


# NOTE: if a function includes a ** parameter and a positional keyword, the
# a is a positional argument, c is a positional argument with a default,
# b collects arbitrary positional arguments, and d collects arbitrary keyword
# arguments
def f2(a, b=6, *c, **d):
    print(a, b, c, d)


if __name__ == '__main__':
    print('code snippets from pages 561-562\n')

    f1(1, 2, 3, x=4, y=5)  # 1 (2,3) 6 {'x':4,'y':5}... uses default for c

    # NOTE: **dict(k=v,...) or **{'k':v,...} can be used to provide keyword
    # arguments
    f1(1, *(2, 3), **dict(x=4, y=5))  # same as ^^^
    f1(1, *(2, 3), **{'x': 4, 'y': 5})  # same as ^^^
    f1(1, 2, 3, x=4, y=5, c=7)  # 1 (2,3) 7 {'x':4,'y':5}.. overrides default c
    f1(1, 2, 3, c=7, x=4, y=5)  # 1 (2,3) 7 {'x':4,'y':5}.. overrides default c
    f1(1, *(2, 3), c=7, **dict(x=4, y=5))  # same as ^^^
    f1(1, c=7, *(2, 3), **dict(x=4, y=5))  # same as ^^^
    f1(1, c=7, *(2, 3), x=4, y=5)  # same as ^^

    # NOTE: a keyword-only arguments may be packed into ** arguments
    f1(1, *(2, 3), **dict(x=4, y=5, c=7))  # same as ^^^
    f1(1, *(2, 3), **{'x': 4, 'y': 5, 'c': 7})  # same as ^^^

    # NOTE: since c is a keyword-only argument it can be passed after **
    # arguments
    f1(1, *(2, 3), **dict(x=4, y=5), c=7)  # same as ^^^
    print('')

    f1(1, c=7)  # 1 () 7 {}
    f1(1, **{'c': 7})  # same as ^^^
    f1(1, **dict(c=7))  # same as ^^^
    print('')

    f2(1)  # 1 6 () {}... uses defaults for b, c, and d
    f2(1, 7, 3, x=5)  # 1 7 (3,) {'x':5}... overrides default b by position
    f2(1, **{'b': 7})  # 1 7... overrides b when ** is unpacked
    f2(1, **{'b': 7, 'x': 4, 'y': 5})  # 1 7 () {'x':4,'y':5}
    f2(1, **{'x': 4, 'b': 7, 'y': 5})  # same as ^^^
    print('')

    # NOTE: since b is not a keyword-only argument, it cannot be passed after
    # ** arguments
    try:
        f2(1, *(2, 3), **dict(x=4, y=5), b=7)
    except TypeError as ex:
        print(ex)
