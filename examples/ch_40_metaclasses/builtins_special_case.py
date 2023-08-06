# usage: python3 builtins_special_case.py

class C1:
    attr = 1

    def __str__(self):
        return ('class')


class D2(type):
    def __str__(self):
        return ('D2 class')


class C21(D2):
    pass


class C22(D2):
    def __str__(self):
        return ('C22 class')


class C23(metaclass=D2):
    def __str__(self):
        return ('C23 class')


class C24(metaclass=D2):
    pass


if __name__ == '__main__':
    print('code snippets from pages 1434-1435\n')

    I1 = C1()

    print(I1.__str__())  # class
    print(str(I1))  # class
    print('')
    
    I1.__str__ = lambda: 'instance'

    print(I1.__str__())  # instance (explicit)
    print(str(I1))  # class (built-in)
    print('')

    print(I1.attr)  # 1
    
    I1.attr = 2

    print(I1.attr)  # 2
    print('')

    print(C21.__str__(C21))  # D2 class (super)
    print(str(C21))  # <class '__main__.C2'>  (metaclass)
    print('')

    print(C22.__str__(C22))  # C22 (class)
    print(str(C22))  # <class '__main__.C22'> (metaclass)
    print('')

    print(C23.__str__(C23))  # C23 class (user-defined)
    print(str(C23))  # D2 class (user-defined)
    print('')

    print(C24.__str__(C24))  # <class '__main__.C24'> (object)
    print(str(C24))  # D2 class (metaclass)
    print('')

    print(C24.__str__)  # <slot wrapper '__str__' of 'object' objects>
    print('')

    # ['C24', 'object']
    # ['D2', 'type', 'object']
    # ['type', 'object']
    for k in (C24, C24.__class__, type):
        print([x.__name__ for x in k.__mro__])
    print('')

