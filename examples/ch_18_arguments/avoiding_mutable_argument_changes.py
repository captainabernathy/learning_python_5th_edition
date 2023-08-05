# usage: python3 avoiding_mutable_argument_changes.py

def changer(a, b):
    # since a does not receive a mutable type, this change is local to
    # this function
    a = 2  # updates local copy of a
    # since b receives a mutable type, this update changes b in place
    b[0] = a * 'spam'  # changes b in place


if __name__ == '__main__':
    print('code snippets from page 547\n')

    X = 1
    L = [1, 2]
    D = {'a': 1}
    print(X)  # 1
    print(L)  # [1,2]
    print(D)  # {'a':1}
    print('')

    # NOTE: to avoid a function changing a mutable type, pass it a copy
    changer(X, L[:])  # function only changes the copy of L it receives
    print(X)  # 1... unchanged
    print(L)  # [1,2]... unchanged
    print('')

    changer(X, D.copy())  # function only changes the copy of D it receives
    print(X)  # 1... unchanged
    print(D)  # {'a':1}... unchanged
    print('')

    # NOTE: if a function attempts to change a mutable type, it will cause an
    # error
    try:
        changer(X, tuple(L))  # error!
    except TypeError as ex:
        print(ex)
