# usage: python3 constraint_call_chain_anchor_requirement.py

class B1:
    def __init__(self):
        print('B1.__init__')
        super().__init__()


class C1:
    def __init__(self):
        print('C1.__init__')
        super().__init__()


# NOTE: D1 inherits B1.__init__() but B1's MRO differs for D1...
# works only bc the implied object at the end of the MRO of all three
# classes happens to have a compatible __init__()
# The rules for such dispatch are:
# 1. super() exists
# 2. __init__() has the same signature across the tree
# 3. every __init__() except the last uses super() itself
class D1(B1, C1):
    pass


class B2:
    def __init__(self):
        print('B2.__init__')


class C2:
    def __init__(self):
        print('C2.__init__')


class D2(B2, C2):
    def __init__(self):
        B2.__init__(self)  # explicit dispatch... doesn't rely on rules above
        C2.__init__(self)


if __name__ == '__main__':
    print('code snippets from pages 1089-1090\n')

    x = B1()  # B1.__init__
    print('')

    x = C1()  # C1.__init__
    print('')

    x = D1()  # B1.__init__, C1.__init__
    print('')

    # (<class '__main__.B1'>, <class 'object'>)
    print(B1.__mro__)
    print('')

    # (<class '__main__.D1'>, <class '__main__.B1'>, <class '__main__.C1'>,
    #  <class 'object'>)
    print(D1.__mro__)
    print('')

    x = D2()  # B2.__init__, C2.__init__
