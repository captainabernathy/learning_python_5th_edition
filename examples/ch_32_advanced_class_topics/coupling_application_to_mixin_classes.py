# usage: python3 coupling_application_to_mixin_classes.py

# mixins work for disjoint method sets
class A1:
    def other(self):
        print('A1.other')


class Mixin1(A1):
    def other(self):
        print('Mixin1.other')
        super().other()  # calls A1.other()


class B1:
    def method(self):
        print('B1.method')


class C1(Mixin1, B1):
    def method(self):
        print('C1.method')
        super().other()  # calls Mixin1().other()... B1 has no other()
        super().method()  # calls B1.method()... Mixin1 has no method()


# other orderings work too
class C11(B1, Mixin1):
    def method(self):
        print('C11.method')
        super().other()  # calls Mixin1().other()... B1 has no other()
        super().method()  # calls B1.method()... Mixin1 has no method()


# explicit diamonds work
class A2:
    def other(self):
        print('A2.other')


class Mixin2(A2):
    def other(self):
        print('Mixin2.other')
        super().other()  # calls A2.other()


class B2(A2):
    def method(self):
        print('B2.method')


# other orderings work too
class C2(Mixin2, B2):
    def method(self):
        print('C2.method')
        super().other()  # calls Mixin2.other()... B2 has no other()
        super().method()  # calls B2.method()... Mixin2 has no method()


class C22(B2, Mixin2):
    def method(self):
        print('C22.method')
        super().other()  # calls Mixin2.other()... B2 has no other()
        super().method()  # calls B2.method()... Mixin2 has no method()


class C222(Mixin2, B2):
    def method(self):
        print('C222.method')
        # makes explicit calls instead of using super()
        Mixin2.other(self)  # better/more clear than above
        B2.method(self)


# for nondisjoint methods: super creates overly strong coupling
class A3:
    def method(self):
        print('A3.method')


class Mixin3(A3):
    def method(self):
        print('Mixin3.method')
        super().method()  # calls A3.method()


class B3(A3):
    def method(self):  # breaks chain of propagation
        print('B3.method')


class C3(Mixin3, B3):
    def method(self):
        print('C3.method')
        super().method()  # A3.method() never called bc B3 doesn't call super()


# NOTE: explicit calls are immune to context
class Mixin33(A3):
    def method(self):
        print('Mixin33.method')
        A3.method(self)  # explicit


# NOTE: explicit calls are immune to context
class C33(Mixin33, B3):
    def method(self):
        print('C33.method')
        Mixin33.method(self)  # explicit


if __name__ == '__main__':
    print('code snippets from pages 1093-1095\n')

    # Mix-ins work for disjoint method sets
    # C1 is a (Mixin1, B1)... Mixin1 is an A1
    C1().method()  # C1.method Mixin1.other A1.other B1.method
    print('')

    # (<class '__main__.C1'>,<class '__main__.Mixin1'>,<class '__main__.A1'>,
    #  <class '__main__.B1'>,<class 'object'>
    print(C1.__mro__)
    print('')

    # C11 is a (B1, Mixin1)... Mixin1 is an A1
    C11().method()  # C11.method Mixin1.other A1.other B1.method
    print('')

    # (<class '__main__.C11'>,<class '__main__.B1'>,<class '__main__.Mixin1'>,
    #  <class '_main__.A1'>,<class 'object'>)
    print(C11.__mro__)
    print('')

    # C2 is a (Mixin2, B2)... Mixin2 is an A2, and B2 is an A2
    C2().method()  # C2.method Mixin2.other A2.other B2.method
    print('')

    # (<class '__main__.C2'>,<class '__main__.Mixin2'>,<class '__main__.B2'>,
    #  <class '__main__.A2'>,<class 'object'>)
    print(C2.__mro__)
    print('')

    # C22 is a (B2, Mixin2)... B2 is an A2, and Mixin2 is an A2
    C22().method()  # C22.method Mixin2.other A2.other B2.method
    print('')

    # (<class '__main__.C22'>,<class '__main__.B2'>,<class '__main__.Mixin2'>,
    #  <class '__main__.A2'>,<class 'object'>)
    print(C22.__mro__)
    print('')

    # C222 is a (Mixin2, B2)... Mixin2 is an A2, and B2 is an A2
    C222().method()  # C222.method Mixin2.other A2.other B2.method
    print('')

    # (<class '__main__.C222'>,<class '__main__.Mixin2'>,<class '__main__.B2'>,
    #  <class '__main__.A2>, <class 'object'>)
    print(C222.__mro__)
    print('')

    # Mixin3 is an A3
    Mixin3().method()  # Mixin3.method A3.method
    print('')

    # C3 is a (Mixin3, B3)... Mixin3 is an A3, and B3 is an A3
    # NOTE: A3.method not called since B3 doesn't call super
    C3().method()  # C3.method Mixin3.method B3.method
    print('')

    # C33 is a (Mixin33, B3)... Mixin33 is an A3, and B3 is an A3
    # NOTE:  C33's method() explicitly calls Mixin33's method(), which
    # explicitly calls A3's method()
    C33().method()  # C33.method Mixin33.method A3.method
