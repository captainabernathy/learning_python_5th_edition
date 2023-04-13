X = 1


def nester1():
    print(X)  # global X

    # nested class
    class C:
        print(X)  # global X

        def method1(self):
            print(X)  # global X

        def method2(self):
            X = 3  # method local.. hides global
            print(X)  # 3

    N = C()  # 1
    N.method1()  # 1
    N.method2()  # 3


def nester2():
    X = 2  # function's local X... hides global X
    print(X)  # 2

    # nested class
    class C:
        print(X)  # 2... accesses function's local X

        def method1(self):
            print(X)  # 2... accesses enclosing local X

        def method2(self):
            X = 3  # method's local X
            print(X)  # 3

    N = C()  # 2
    N.method1()  # 2
    N.method2()  # 3


def nester3():
    X = 2  # function's local X... hides global X
    print(X)  # 2

    class C:
        # class's local X... hides function's local X: C.X or I.X (not scoped)
        X = 3
        print(X)  # 3

        def method1(self):
            print(X)  # 2... accesses function's local X... NOT class's local X
            print(self.X)  # class local X... 3

        def method2(self):
            # method's local X.. hides function's local X.. NOT class's local X
            X = 4
            print(X)
            self.X = 5   # updates instance's X
            print(self.X)

    N = C()  # 3... accesses class's local X
    N.method1()  # 2 3... accesses function's local X
    N.method2()  # 4 5... accesses method's local X and update's instance's X
    N2 = C()  # 3... accesses class's local X
    print(N2.X)  # 3... access class's local X directly


if __name__ == '__main__':
    print('code snippets from pages 905-906\n')
    print(X)  # 1
    nester1()  # 1 1 1 3
    print('-' * 40)

    print(X)  # 1
    nester2()  # 2 2 2 3
    print('-' * 40)

    print(X)  # 1
    nester3()  # 2 3 2 3 4 5 3
