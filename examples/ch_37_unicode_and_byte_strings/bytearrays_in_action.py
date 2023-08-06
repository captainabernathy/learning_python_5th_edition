# usage: python3 bytearrays_in_action.py

if __name__ == '__main__':
    print('code snippets from pages 1233-1235\n')

    # bytearrays are mutable sequences of integers in the ragne 0-255
    S = 'spam'
    try:
        C = bytearray(S)  # OK in 2X, but not 3X
    except TypeError as ex:
        print(ex)  # string argument without an encoding
    print('')

    C = bytearray(S, 'latin1')  # 3X requires encoding
    print(C)  # bytearray(b'spam')
    print('')

    B = b'spam'
    C = bytearray(B)  # ok here bc B is a bytes (not a string) object
    print(C)  # bytearray(b'spam')
    print('')

    print(C[0])  # 115 indexing into bytearray
    print('')

    try:
        C[0] = 'x'  # error... can't assign string to bytearray!!!
    except TypeError as ex:
        print(ex)  # 'str' object cannot be interpreted as an integer
    print('')

    try:
        C[0] = b's'  # error... bytes cannot be interpreted as an integer
    except TypeError as ex:
        print(ex)  # 'bytes' object cannot be interpreted as an integer
    print('')

    C[0] = ord('x')  # requires integer code point
    print(C)  # bytearray(b'xpam')
    print('')

    C[1] = b'Y'[0]  # getting index of byte string returns code point
    print(C)  # bytearray(b'xYam')
    print('')

    # in bytes but not bytearray...
    # {'__getnewargs__'}
    print(set(dir(b'abc')) - set(dir(bytearray(b'abc'))))
    print('')

    # in bytearray but not bytes...
    # {'pop', '__iadd__', 'reverse', '__imul__', 'copy', 'append', 'insert',
    #  '__alloc__', 'clear', '__delitem__', 'extend', '__setitem__', 'remove'}
    print(set(dir(bytearray(b'abc'))) - set(dir(b'abc')))
    print('')

    # mutable method calls
    try:
        C.append(b'LMN')  # error...
    except TypeError as ex:
        print(ex)  # bytes cannot be interpreted as an integer
    print('')

    C.append(ord('L'))
    print(C)  # bytearray(b'xYamL')
    print('')

    C.extend(b'MNO')  # extend is ok
    print(C)  # bytearray(b'xYamLMNO')
    print('')

    print(C + b'!#')  # bytearray(b'xYamLMNO!#') concatenation
    print('')

    print(C[0])  # 120... integer point code
    print('')

    print(C[1:])  # bytearray(b'YamLMNO')... slicing
    print('')

    print(len(C))  # 8
    print('')

    try:
        C.replace('xY', 'sp')  # doesn't work in 3X
    except TypeError as ex:
        print(ex)  # a bytes-like object is required, not 'str'
    print('')

    print(C.replace(b'xY', b'sp'))  # bytearray(b'spamLMNO')... ok
    print(C)  # bytearray(b'xYamLMNO')
    print('')

    # bytearray(b'xYamLMNOxYamLMNOxYamLMNOxYamLMNO')
    print(C * 4)  # repetition
