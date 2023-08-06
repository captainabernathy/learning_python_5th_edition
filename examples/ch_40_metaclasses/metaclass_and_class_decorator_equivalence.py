# usage: python3 metaclass_and_class_decorator_equivalence.py

# NOTE:
#   - because decorators run after a class is created, they incur an extra
#     runtime step in class creation roles
#
#   - because metaclass must create classes, they incur an extra coding step in
#     instance management roles


class Metaclass(type):
    def __new__(meta, clsname, supers, attrdict):
        print('In M.__new__:')
        print([clsname, supers, list(attrdict.keys())])
        print('')
        return type.__new__(meta, clsname, supers, attrdict)


def decorator(cls):
    return Metaclass(cls.__name__, cls.__bases__, dict(cls.__dict__))


class A:
    x = 1


print('code snippets from page 1445\n')


# NOTE: class decorator returns a metaclass instance
@decorator
class B(A):  # B(A) = decorator(B)(A)
    y = 2

    def m(self):
        return self.x + self.y


def func1(name, supers, attrs):
    return 'spam'


class C1(metaclass=func1):
    attr = 'huh?'


def func2(cls):
    return 'spam'


@func2
class C2:  # C2 = func(C2)
    attr = 'huh?'


if __name__ == '__main__':
    print(B.x)  # 1
    print(B.y)  # 2
    print('')

    I1 = B()

    print(I1.x)  # 1
    print(I1.y)  # 2
    print(I1.m())  # 3
    print('')

    print(C1)  # spam
    print(C1.upper())  # SPAM
    print('')

    print(C2)  # spam
    print(C2.upper())  # SPAM

