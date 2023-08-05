# usage: python3 testmixin.py

import importlib


def tester(listerclass, sept=False):

    class Super:
        def __init__(self):
            self.data1 = 'spam'  # instance attr

        def ham(self):  # bound method
            pass

    class Sub(Super, listerclass):  # Mixin ham and a __str__()
        def __init__(self):  # listers have access to self
            Super.__init__(self)  # call Super()'s constructor
            self.data2 = 'eggs'  # more instance attrs
            self.data3 = 42

        def spam(self):  # bound method
            pass

    instance = Sub()  # return instance with lister's __str__
    print(instance)  # run mixin's __str__() (or via str(x))

    if sept:
        print('-' * 80)


def test_by_name(modname, classname, sept=False):
    modobject = importlib.import_module(modname)  # Import by namestring
    listerclass = getattr(modobject, classname)  # fetch attr by namestring
    tester(listerclass, sept)


if __name__ == '__main__':
    print('code snippets from pages 994-995\n')

    test_by_name('listinstance', 'ListInstance', True)
    test_by_name('listinherited', 'ListInherited', True)
    test_by_name('listtree', 'ListTree', False)
