# NOTE: __call__() overrides the function call operator
class Callee:
    def __call__(self, *pargs, **kargs):
        print('Called:', pargs, kargs)


class C1:
    def __call__(self, a, b, c=5, d=6):
        print('C1: ', a, b, c, d)


class C2:
    def __call__(self, *pargs, **kargs):
        print('C2:', pargs, kargs)


class C3:
    def __call__(self, *pargs, d=6, **kargs):
        print('C3:', pargs, d, kargs)


class Prod1:
    def __init__(self, value):
        self.value = value

    def __call__(self, other):
        return self.value * other


class Prod2:
    def __init__(self, value):
        self.value = value

    def comp(self, other):  # same functionality as __call__ above
        return self.value * other


if __name__ == '__main__':
    print('code snippets from pages 950-952\n')
    C = Callee()
    C(1, 2, 3)  # Called: (1,2,3) {}
    C(1, 2, 3, x=4, y=5, z='Sally')  # Called: (1,2,3){'x':4,'y':5,'z':'Sally'}
    print('')

    C_1 = C1()
    C_1(1, 2, 3, 4)  # C1: 1 2 3 4
    C_1(1, 2, c=4, d=5)  # C1: 1 2 4 5
    print('')

    C_2 = C2()
    C_2(1, 2, 3, 4)  # C2: (1,2,3,4){}
    C_2(1, 2, c=4, d=5)  # C2: (1,2){'c':4,'d':5}
    print('')

    C_3 = C3()
    C_3(1, 2, 3, d=4, a=1, b=2)  # C3: (1,2,3)4{'a':1,'b':2}
    C_3(d=6)  # () 6 {}
    print('')

    x = Prod1(2)
    print(x.value)  # 2
    print(x(3))  # 6
    print(x(4))  # 8
    print('')

    x = Prod2(3)
    print(x.value)  # 3
    print(x.comp(3))  # 9
    print(x.comp(4))  # 12
