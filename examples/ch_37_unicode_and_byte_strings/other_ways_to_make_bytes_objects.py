if __name__ == '__main__':
    print('code snippets from page 1232\n')

    B = b'abc'
    print(B)  # b'abc'
    print('')

    B = bytes('abc', 'ascii')  # constructor requires encoding name
    print(B)  # b'abc'
    print('')

    print(ord('a'))  # code point for 'a'... 97
    print('')

    B = bytes([97, 98, 99])  # constructor with iterable integers
    print(B)  # b'abc'

    B = bytes((97, 98, 99))
    print(B)  # b'abc'
    print('')

    B = 'spam'.encode()  # encode str to bytes
    print(B)  # b'spam'
    print('')

    S = B.decode()  # decode bytes to str
    print(S)  # spam
    print('')
