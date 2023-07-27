if __name__ == '__main__':
    print('code snippets from pages 1215-1216\n')

    B = b'spam'  # byte literal makes a bytes object
    S = 'eggs'  # string literal makes a unicode string

    print(type(B), type(S))  # <class 'bytes'> <class 'str'>
    print(B)  # b'spam'
    print(S)  # eggs
    print('')

    # bytes object is a sequence of short integers
    print(B[0], S[0])  # 115, e
    # slicing makes another bytes or string object
    print(B[1:], S[1:])  # b'pam', ggs
    print(list(B), list(S))  # [115,112,97,109] ['e','g','g','s']
    print('')

    # NOTE: bytes and string objects are immutable
    try:
        B[0] = 'x'
    except TypeError as ex:
        print(ex)  # 'bytes' object does not support item assignment
    print('')

    try:
        S[0] = 'x'
    except TypeError as ex:
        print(ex)  # 'str' object does not support item assignment
    print('')

    # bytes works on triple quoted strings
    b = b'''
xxx
yyy
'''
    print(b)  # b'\nxxx\nyyy\n'
    print('')

    # python 2x Unicode Literals are accepted in Python 3.3+
    U = u'spam'  # works in 3x but is (redundant) just a string
    print(type(U))  # <class 'str'>
    print(U)  # spam
    print(U[0])  # s
    print(list(U))  # ['s','p','a','m']
    print('')
