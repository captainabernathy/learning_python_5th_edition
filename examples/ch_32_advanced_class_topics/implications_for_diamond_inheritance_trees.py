# old style class in 2X, new style class in 3X
class A:
    attr = 1


# B is an A, and A is an old style class in 2X but a new style class in 3X
class B(A):
    pass


# C is an A, and A is an old style class in 2X but a new style class in 3X
class C(A):
    attr = 2


# D is a B and a C, and both B and C are an A, and A is an old style class
# in 2X but a new style class in 3X, so...
# in 2X D searches B first, then A, then C
# in 3X D searches B first, then C, then A
class D(B, C):
    pass


# NA is a new style class in 2X and 3X
class NA(object):
    attr = 1


# NB is an NA
class NB(NA):
    pass


# NC is an NA
class NC(NA):
    attr = 2


# ND is an NB and an NC, and both NB and NC are an NA, and NA is a new style
# class so...
# ND searches NB first, then NC, then NA in both 2X and 3X
class ND(NB, NC):
    pass


if __name__ == '__main__':
    print('code snippets from page 1033\n')

    x = D()

    print(x.attr)  # 1... 2X found in A, 2... 3X found in C
    print('')

    nx = ND()
    print(nx.attr)  # 2...  2X and 3X found in C
    print('')
