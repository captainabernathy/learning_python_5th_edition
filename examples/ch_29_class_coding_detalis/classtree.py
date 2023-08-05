# usage: python3 classtree.py

'''
module provides functions that climb inheritance trees using namespace links
displaying higher superclasses with indentation for height
'''


def classtree(cls, indent):
    print('.' * indent + cls.__name__)  # print class name
    for supercls in cls.__bases__:
        classtree(supercls, indent + 3)  # may visit super class more than once


def instancetree(inst):
    print('Tree of %s' % inst)  # print instance
    classtree(inst.__class__, 3)  # climb to its class


def selftest():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B, C):
        pass

    class E:
        pass

    class F(D, E):
        pass

    instancetree(B())
    instancetree(F())


if __name__ == '__main__':
    print('code snippets from page 909\n')

    selftest()
