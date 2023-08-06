# usage: python3 metaclass_methods.py

class A(type):
    def x(cls):
        print('ax', cls)

    def y(cls):
        print('ay', cls)


class B(metaclass=A):
    def y(self):
        print('by', self)

    def z(self):
        print('bz', self)


if __name__ == '__main__':
    print('code snippets from pages 1435-1436\n')

    # NOTE: metaclass methods process their instance classes... not instance
    # objects

    print(B.x)  # <bound method of A.x of <class '__main__.B'>>... acquired
                # from metaclass
    print('')

    print(B.y)  # <function B.y at 0x...>... defined in class
    print('')

    print(B.z)  # <function B.z at 0x...>... defined in class
    print('')

    B.x()  # ax <class '__main__.B'>... method call gets class
    A.x(B)  # same as ^^^
    print('')

    I1 = B()

    I1.y()  # by <__main__.B object at 0x...>
    print('')

    I1.z()  # bz <__main__.B object at 0x...>
    print('')

    try:
        I1.x()  # ERROR... instance can't access metaclass names
    except AttributeError as ex:
        print(ex)  # 'B' object has no attribute 'x'
    print('')

