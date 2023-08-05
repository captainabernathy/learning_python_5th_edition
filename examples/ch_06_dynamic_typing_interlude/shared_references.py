# usage: python3 shared_references.py

import sys

if __name__ == '__main__':
    print('code snippets from pages 186-191\n')

    a = 3  # a is an integer
    b = a  # b is a reference to the integer assigned to a
    print("a:", a, " b:", b)  # 3, 3

    a = 'spam'  # a is now a string
    print("a:", a, " b:", b)  # 'spam', 3

    a = b  # a now references the object b references (3)
    a = a + 2  # a now references an integer object whose value is 5
    print("a:", a, " b:", b)  # 5, 3
    print('')

    L1 = [2, 3, 4]  # L1 refers to a list
    L2 = L1  # L2 and L1 refer to the same list
    print("L1:", L1)  # [2,3,4]
    print("L2:", L2)  # [2,3,4]
    print('')

    L1 = 24  # L1 now refers to an integer
    print("L1:", L1)  # 24
    print("L2:", L2)  # [2,3,4]
    print('')

    L1 = L2  # L1 referes to L2, which refers to a list
    # change the object in the list at index 0 that both L1 and L2 refernece
    L1[0] = 24
    print("L1:", L1)  # [24,3,4]
    print("L2:", L2)  # [24,3,4]
    print('')

    # change the object in the list at index 1 that both L1 and L2 refernece
    L2[1] = 97
    print("L1:", L1)  # [24,97,4]
    print("L2:", L2)  # [24,97,4]
    print('')

    L1 = [2, 3, 4]  # L1 now refers to a new list
    print("L1:", L1)  # [2,3,4]
    print("L2:", L2)  # [24,97,4]
    print('')

    # top-level copy of values from L1 into L2
    # L2 = L1[:] is the same as L2 = copy.copy(L1) or L2 = list(L1)
    L2 = L1[:]  # L1 and L2 refer to individual lists that have the same values
    print("L1:", L1)  # [2,3,4]
    print("L2:", L2)  # [2,3,4]
    print('')

    L1[0] = 24  # does not change L2
    print("L1:", L1)  # [24,3,4]
    print("L2:", L2)  # [2,3,4]
    print('')

    L = [1, 2, 3]
    M = L  # refers to L, which refers to a list
    print("L:", L)  # [1,2,3]
    print("M:", M)  # [1,2,3]

    # NOTE: == tests if two objects have same value
    print("L == M:", L == M)  # True

    # NOTE: is tests if two names refer to the same object
    print("L is M:", L is M)  # True
    print('')

    M = [1, 2, 3]  # M now refers to a list that contains the same values as L
    print("L:", L)  # [1,2,3]
    print("M:", M)  # [1,2,3]
    print("L == M:", L == M)  # True
    print("L is M:", L is M)  # False
    print('')

    X = 42  # X refers to integer object
    Y = 42  # Y refers to an integer object with the same value as X
    print("X:", X, " Y:", Y)  # 42, 42

    # NOTE: python chaches and reuses integers and strings, so...
    # the is operator may not always produce the expected result
    print("X == Y:", X == Y)  # True
    print("X is Y", X is Y)  # True due to caching
    print('')

    # NOTE: sys.getrefcount(obj) returns the numbers of pointers that
    # reference obj
    print(sys.getrefcount(L))  # number of pointers to shared piece of memory
