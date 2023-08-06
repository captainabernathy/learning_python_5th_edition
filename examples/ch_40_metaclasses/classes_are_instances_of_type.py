# usage: python3 classes_are_instances_of_type.py

from __future__ import print_function


class C:
    pass


class D(object):
    pass


if __name__ == '__main__':
    print('code snippets from pages 1411-1413\n')

    # NOTE: in 2X type is a unique kind of built-in object that caps the type
    # hierarchy and is used to construct types...
    #
    # in 3X:
    #   a) types are defined by classes (that derive from them)
    #   b) classes are instances of type (classes)
    #   c) classes are types that generate instances of their own

    print(type([]))  # <class 'list'>... in 3X... <type 'list'>... in 2X
    print(type(type([])))  # <class 'type'>... in 3X... <type 'list'>... in 2X
    print('')

    print(type(list))  # <class 'type'>... in 3X... <type 'type'>... in 2X
    print(type(type))  # <class 'type'>... in 3X... <type 'type'>... in 2X
    print('')

    # NOTE: in 3X and new style classes in 2X, classes have a __class__
    # attribute that links to type, and an instance of a class has a __class__
    # attribute that links to the class from which it was made
    X = C()

    print(type(X))  # <class '__main__.C'>... 3X... <type 'instance'>... 2X
    print(X.__class__)  # <class '__main__.C'>... 3X... __main__.C ... 2X
    print('')

    print(type(C))  # <class 'type'>... 3X... <type 'classobj'>
    try:
        print(C.__class__)  # <class 'type'>... in 3X... ERROR in 2X
    except AttributeError as ex:
        print(ex)  # AttributeError: class C has no attribute '__class__'
    print('')

    X = D()
    print(type(X))  # <class '__main__.D'>
    print(X.__class__)  # <class '__main__.D'>
    print('')

    print(type(D))  # <class 'type'>... 3X... <type 'type'>... 2X
    print(D.__class__)  # <class 'type'>... 3X... <type 'type'>... 2X
    print('')

