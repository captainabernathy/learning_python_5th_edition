# usage: python3 operator_overloading_in_metaclass_methods.py

class A1(type):
    # NOTE: here, __getitem__() is a metaclass method designed to process
    # classes themselves (ie: the classes that are instances of the metaclass,
    # NOT those classes' own later instances)
    def __getitem__(cls, i):
        return cls.data[i]


class B1(metaclass=A1):
    data = 'spam'


class A2(type):
    # NOTE: similarly, __getattr__() processes instance classes only... NOT
    # their normal instances
    def __getattr__(cls, name):
        return getattr(cls.data, name)

    
class B2(metaclass=A2):
    data = 'spam'


if __name__ == '__main__':
    print('code snippets from pages 1437-1438\n')

    print(B1[0])  # s
    print('')

    # <bound method A1.__getitem__ of <class '__main__.B1'>>
    print(B1.__getitem__)
    print('')

    I1 = B1()

    print(I1.data)  # spam
    print(B1.data)  # spam
    print('')

    try:
        I1[0]  # ERROR... __getitem__() not accessible through instance
    except TypeError as ex:
        print(ex)  # 'B1' object is not subscriptable
    print('')

    print(B2.upper())  # SPAM
    print('')

    print(B2.upper)  # <built-in method upper of str object at 0x...>
    print('')

    # <bound method A2.__getattr__ of <class '__main__.B2'>>
    print(B2.__getattr__)
    print('')

    I2 = B2()

    try:
        I2.upper()  # ERROR
    except AttributeError as ex:
        print(ex)  # 'B2' object has no attribute 'upper'
    print('')

    try:
        I2.__getattr__  # ERROR: not acquired by class instance
    except AttributeError as ex:
        print(ex)  # 'B2' object has no attribute '__getattr__'
    print('')

    B2.data = [1, 2, 3]
    B2.append(4)

    print(B2.data)  # [1,2,3,4]
    print('')

    print(B2.__getitem__(0))  # 1
    print('')

    try:
        print(B2[0])  # list[0]... ???
    except TypeError as ex:
        print(ex)
    print('')

