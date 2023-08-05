# usage: python(2/3) all_classes_derive_from_object.py

from __future__ import print_function

# NOTE: a type object's type is type and object's type is type... and a type
# object is an instance of object... and object is an instance of type


# old style class in 2X, new style class in 3X
class C:
    pass


if __name__ == '__main__':
    print('code snippets from pages 1030-1031\n')

    X = C()

    # <type 'instance'> <type 'classobj'>... 2X
    # <class '__main__.C> <class 'type'>... 3X
    print(type(X), type(C))
    print('')

    print(isinstance(X, object))  # True... 2X and 3X
    print(isinstance(C, object))  # True... 2X and 3X
    print('')

    # <type 'str'> <type 'type'>... 2X
    # <class 'str'> <class 'type'>... 3X
    print(type('spam'), type(str))
    print('')

    print(isinstance('spam', object))  # True... 2X and 3X
    print(isinstance(str, object))  # True... 2X and 3X
    print('')

    # <type 'type'> <type 'type'>... 2X
    # <class 'type'> <class 'type'>... 3X
    print(type(type), type.__class__)

    # <type 'type'> <type 'type'>... 2X
    # <class 'type'> <class 'type'>... 3X
    print(type(object), object.__class__)
    print('')

    # all classes derive from object... even type
    print(isinstance(type, object))  # True... 2X and 3X
    print('')

    # types make classes
    print(isinstance(object, type))  # True... 2X and 3X
    print('')

    print(type is object)  # False... 2X and 3X
    print('')
