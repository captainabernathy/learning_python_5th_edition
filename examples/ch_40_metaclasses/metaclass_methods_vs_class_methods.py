# usage: python3 metaclass_methods_vs_class_methods.py

class A(type):
    def a(cls):
        cls.x = cls.y + cls.z


class B(metaclass=A):
    y, z = 11, 22

    @classmethod
    def b(cls):
        return cls.x


if __name__ == '__main__':
    print('code snippets from page 1436\n')

    # NOTE: metaclass methods are designed to manage class-level data

    B.a()  # creates class data on B, accessible to normal instances
    print('')

    print(B.x)  # 33
    print('')

    I1 = B()

    print(I1.x)  # 33
    print(I1.y)  # 11
    print(I1.z)  # 22
    print('')

    print(I1.b())  # 33
    print('')

    try:
        I1.a()  # ERROR: metaclass methods accessible through the class only
    except AttributeError as ex:
        print(ex)  # 'B' object has no attribute 'a'
    print('')

