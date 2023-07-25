from __future__ import print_function


# old style class in 2X, new style class in 3X
class C:
    pass


# new style class in both 2X and 3X
class NC(object):
    pass


if __name__ == '__main__':
    print('code snippets from page 1031\n')

    print(dir(object))
    print('')

    # ()... 2X... classes do not inherit from object by default
    # (<class 'object'>,)  # in 3X
    print(C.__bases__)
    print('')

    X = C()
    try:
        print(X.__repr__)  # <method-wrapper '__repr__' of C ...> in 3X
    except AttributeError as ex:
        print(ex)  # C instance hos no attribute '__repr__' 2X
    print('')

    # (<type 'object'>,)... 2X
    # (<class 'object'>,)... 3X
    print(NC.__bases__)
    print('')

    NX = NC()
    # <method-wrapper '__repr__' of NC ...>... 2X and 3X
    print(NX.__repr__)
