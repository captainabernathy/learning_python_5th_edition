class X1:
    a = 1  # class attribute


class X2:
    pass


class Y2:
    pass


class Record:
    pass


if __name__ == '__main__':
    print('code snippets from pages 1101-1102\n')

    i = X1()
    print(X1.a)  # 1
    print(i.a)  # 1... inherited by instance
    print('')

    X1.a = 2  # may change more than X
    print(X1.a)  # 2
    print(i.a)  # 2
    print('')

    i.a *= 2
    print(X1.a)  # 2
    print(i.a)  # 4
    print('')

    j = X1()
    print(X1.a)  # 2
    print(i.a)  # 4
    print(j.a)  # 2... inherited fron class
    print('')

    j.a *= 3
    print(X1.a)  # 2
    print(i.a)  # 4
    print(j.a)  # 6
    print('')

    X1.a /= 2
    print(X1.a)  # 1
    print(i.a)  # 4
    print(j.a)  # 6
    print('')
    
    X2.a = 1
    X2.b = 2
    X2.c = 3
    Y2.a = X2.a + X2.b + X2.c

    for X2.i in range(Y2.a):
        print(X2.i)  # 0 1 2 3 4 5
    print('')

    X = Record()
    X.name = 'bob'
    X.job = 'Pizza Maker'
    print(X.name, X.job)  # bob Pizza Maker
