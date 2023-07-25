from __future__ import print_function

# NOTE: new style classes are types, and types themselves are new style classes


# a classic class in 2X
class C:
    pass


if __name__ == '__main__':
    print('code snippets from pages 1027-1028\n')

    IC = C()
    # <type 'instance'>... 2X... IC is an instance type
    # <class '__main__.C'>... 3X... IC is a type of C
    print(type(IC))

    # __main.__C... 2X... IC's class is C
    # <class '__main__.C'>... 3X... IC's class is C
    print(IC.__class__)
    print('')

    # <type 'classobj'>... 2X... C is a classobj type
    # <class 'type'>... 3x... C is a type
    print(type(C))
    print('')

    try:
        # <class 'type'>...  3X... a class's class type
        print(C.__class__)
    except AttributeError as ex:
        print(ex)  # class C has no attribute '__class__'... 2X
    print('')

    # <type 'list'>... 2X... an instance of a built-in type is the built-in
    # <class 'list'>... 3X... an instance of a built-in type is the built-in
    print(type([1, 2, 3]))

    # <type 'list'>... 2X... the class of an instance of a built-in type is the
    # built-in type
    # <class 'list'>... 3X... the class of an instance of a built-in type is
    # the built-in type
    print([1, 2, 3].__class__)
    print('')

    # <type 'type'>... 2X... a built-in type is a type
    # <class 'type'>... 3X... a built-in type is a type
    print(type(list))

    # <type, 'type'>... 2X... the class of a built-in type is the built-in type
    # <class 'type'>... 3x... the class of a built-in type is the built-in type
    print(list.__class__)
    print('')

    T = C()
    # <type 'instance'>... 2X... T is an instance type
    # <class '.__main__.C'>... 3X... T is a type of C
    print(type(T))

    # __main__.C... 2X... T's class is C
    # <class '__main__.C'>... 3X... T's class is C
    print(T.__class__)
    print('')

    # <type 'classobj'>... 2X... C is a classobj type
    # <class 'type'>... 3X... C is a type
    print(type(C))
    print('')

    try:
        # <class 'type'>... 3X... C's class is type
        print(C.__class__)
    except AttributeError as ex:
        print(ex)  # class C has no attribute '__class__'... 2X

