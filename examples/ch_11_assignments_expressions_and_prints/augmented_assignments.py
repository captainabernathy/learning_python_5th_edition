# usage: python3 augmented_assignments.py

if __name__ == '__main__':
    print('code snippets from pages 360-363\n')

    X = 1
    print(X)  # 1

    X = X + 1
    print(X)  # 2

    X += 1
    print(X)  # 3

    S = 'spam'
    print(S)  # spam

    S += 'SPAM'  # concatenation
    print(S)  # spamSPAM
    print('')

    L = [1, 2]
    print(L)  # [1, 2]
    L = L + [3]  # concatenation... slower
    print(L)  # [1,2,3]

    L.append(4)  # in-place update... faster
    print(L)  # [1,2,3,4]

    L = L + [5, 6]  # concatenation... slower
    print(L)  # [1,2,3,4,5,6]

    # NOTE: A list's extend() method requires a iterable
    L.extend([7, 8])  # in-place update... faster
    print(L)  # [1,2,3,4,5,6,7,8]

    # NOTE: += is overloaded to extend() for a list
    L += [9, 10]  # performs in-place update
    print(L)  # [1,2,3,4,5,6,7,8,9,10]
    print('')

    L = []
    print(L)  # []

    L += 'spam'  # += and extend() work for any sequence, but + does not
    print(L)  # ['s','p','a','m']
    print('')

    L = [1, 2]
    M = L  # M and L share refer to the same object
    print(L, M)  # [1,2] [1,2]

    # NOTE: concatenation creates a new object
    L = L + [3, 4]
    print(L, M)  # [1,2,3,4] [1,2]
    print('')

    L = [1, 2]
    M = L  # shared reference
    print(L, M)  # [1,2] [1,2]

    # NOTE: += and extend() update both variables... since they share the same
    # reference
    L += [3, 4]
    print(L, M)  # [1,2,3,4] [1,2,3,4]

    L = [1, 2]
    M = L
    print(L, M)  # [1,2] [1,2]

    L.extend(M)
    print(L, M)  # [1,2,1,2] [1,2,1,2]
