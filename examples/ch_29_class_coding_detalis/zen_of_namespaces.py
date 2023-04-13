X = 11  # module global


def g1():
    print(X)  # accesses module's X


def g2():
    global X  # grants write access to global scope
    X = 22  # changes module's X


def h1():
    X = 33  # function's local X

    def nested():
        print(X)  # accesses h1's X
    nested()


def h2():
    X = 33  # function's local X

    def nested():
        nonlocal X  # 3X statement to gain write access to an enclosing scope
        X = 44
    nested()
    print(X)


if __name__ == '__main__':
    print('code snippets from pages 903-904\n')
    g1()  # 11... global X
    g2()  # changes global X
    g1()  # 22... reflects change made by g2()
    h1()  # 33... function's local X
    g1()  # still 22
    h2()  # 44... changes function's local X
    g1()  # still 22
