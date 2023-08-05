# usage: python(2/3) explicit_conflict_resolution.py

from __future__ import print_function


# old style class in 2X, new style class in 3X
class A:
    attr = 1

    def meth(self):
        print('A.meth')


# B is an A, and A is an old style class in 2X but a new style class in 3X
class B(A):
    pass


# C is an A, and A is an old style class in 2X but a new style class in 3X
class C(A):
    attr = 2

    def meth(self):
        print('C.meth')


# D is a B and a C, and both B and C are an A, and A is an old style class
# in 2X but a new style class in 3X
class D(B, C):
    attr = C.attr  # choose C... otherwise would choose A in 2X
    # meth = C.meth

    # more clear than ^^^
    def meth(self):
        C.meth(self)


# E is a B and a C, and both B and C are an A, and a is an old style class
# in 2X but a new style class in 3X, so...
# in 2X D searches B first, then A, then C
# in 3X D searches B first, then C, then A
class E(B, C):
    pass


# NA is a new style class in 2X and
class NA(object):
    attr = 1

    def meth(self):
        print('NA.meth')


# NB is an NA
class NB(NA):
    pass


# NC is an NA
class NC(NA):
    attr = 2

    def meth(self):
        print('NC.meth')


# ND is an NB and an NC, and both NB and NC are an NA, and NA is a new
# style class
class ND(NB, NC):
    attr = NB.attr  # chooses NB... otherwise would choose NC in 2X and 3X

    def meth(self):
        NC.meth(self)


# NE is an NB and an NC, and both NB and NC are an NA, and NA is a new
# style class, so...
# NE searches NB first, then NC, then NA
class NE(NB, NC):
    pass


if __name__ == '__main__':
    print('code snippets from pages 1034-1035\n')

    d = D()
    e = E()

    print(d.attr)  # 2... 2X and 3X
    print(e.attr)  # 1... 2X found in A, 2... 3X found in C
    print('')

    d.meth()  # C.meth... 2X and 3X
    e.meth()  # A.meth... 2X, C.meth... 3X
    print('')

    nd = ND()
    ne = NE()

    print(nd.attr)  # 1... 2X and 3X
    print(ne.attr)  # 2... 2X and 3X
    print('')

    nd.meth()  # NC.meth... 2X and 3X
    ne.meth()  # NC.meth... 2X and 3X
    
