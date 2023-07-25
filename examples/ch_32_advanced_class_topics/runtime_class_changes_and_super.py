# class that provides a single method m()
class X:
    def m(self):
        print('X.m')


# class that provides a single method m()
class Y:
    def m(self):
        print('Y.m')


# C1 is an X and overrides the method m()
class C1(X):  # start out inheriting from X
    def m(self):
        super().m()  # can't hardcode class name here


# C2 is an X and overrides the method m()
class C2(X):  # accomplishes the same as ^^^
    def m(self):
        C2.__bases__[0].m(self)


if __name__ == '__main__':
    print('code snippets from pages 1085-1086\n')

    i = C1()
    i.m()  # X.m
    print('')

    # change C1's superclass at runtime
    C1.__bases__ = (Y,)  # C1 is now a Y... NOT an X
    i.m()  # Y.m
    print('')

    i = C2()
    i.m()  # X.m
    print('')

    C2.__bases__ = (Y,)  # C2 is now a Y... NOT and X
    i.m()  # Y.m
