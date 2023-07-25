# NOTE: a namespace __dict__ dict is created when any class in an inheritance
# hierarchy does not define a __slots__ attribute
class C:
    pass


# __slots__ in sub but not super...
# makes instance __dict__ for non-slots... but slot name still managed in class
# NOTE: when a subclass class with slots inherits from a class without
# slots, the instance __dict__ attribute created for its parent class will
# always be accessible
class D(C):
    __slots__ = ['a']


# slots in super but not sub...
# makes instance __dict__ for nonslots
# but slot names still managed in class
class C1:
    __slots__ = ['a']


# NOTE: a __slots__ declaration is limited to the class in which it appears, so
# subclasses will produce an instance __dict__ if they do not define a
# __slots__ attribute
class D1(C1):
    pass


# NOTE: if a class defines a slot that has the same name as a slot in a class
# that it inherits from, the class's slot will hide the slot of the same name
# in its class tree
class C2:
    __slots__ = ['a']


class D2(C2):
    __slots__ = ['a']  # D2 instances can only access this slot


class C3:
    __slots__ = ['a']


class D3(C3):
    __slots__ = ['b']


if __name__ == '__main__':
    print('code snippets from pages 1051-1052\n')

    X = D()
    X.a = 1  # own slot
    X.b = 2  # on X's __dict__... OK since D inherits from C and C has no slots
    print(X.__dict__)  # {'b': 2}
    print(D.__dict__.keys())  # dictkeys([... 'a', '__slots__', ...])
    print('')

    X1 = D1()
    X1.a = 1  # in parent's slot
    X1.b = 2  # on X1's __dict__
    print(X1.__dict__)  # {'b': 2}
    print(C1.__dict__.keys())  # dictkeys([..., 'a', '__slots__', ...])
    print('')

    X2 = D2()  # has no __dict__
    X2.a = 1
    print(X2.__slots__)  # ['a']
    for a in (x for x in dir(X2) if not x.startswith('__')):
        print(a, getattr(X2, a))  # a 1
    print('')

    X3 = D3()  # has no __dict__
    X3.a = 1
    X3.b = 2
    for a in (x for x in dir(X3) if not x.startswith('__')):
        print(a, getattr(X3, a))  # a 1, b 2
    print('')

    # But the classes X3 is derived from have __dict__s
    # dict_keys(['__module__', '__slots__', 'a', '__doc__'])
    print(C3.__dict__.keys())
    
    # dict_keys(['__module__', '__slots__', 'b', '__doc__'])
    print(D3.__dict__.keys())

