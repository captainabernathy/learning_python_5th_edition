# class that only overloads operator [] (__getitem__())
class C:
    # overloads operator "[]"
    def __getitem__(self, ix):
        print('C index')


# D is a C that overrides C's __getitem__() (operator [])
class D(C):
    def __getitem__(self, ix):  # redefine to extend
        print('D index')
        C.__getitem__(self, ix)  # tradition form works
        super().__getitem__(ix)  # direct name calls work too

        # NOTE: the proxy objects returned by super() use
        # __getattribute__() to catch and dispatch later method calls...
        # so they fail to intercept the implicit invocations run by
        # built-in (double underscore) operations...
        try:
            # this fails because
            super()[ix]
        except TypeError as ex:
            print(ex)


if __name__ == '__main__':
    print('code snippets from pages 1082-1083\n')

    X = C()
    X[99]  # C index
    print('')

    X = D()
    X[99]  # D index, C index, C index, 'super' objet is not subscriptable
