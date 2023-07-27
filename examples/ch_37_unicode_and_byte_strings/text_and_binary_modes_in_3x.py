if __name__ == '__main__':
    print('code snippets from pages 1237-1239\n')

    # write and read a text file
    open('temp', 'w').write('abc\n')  # text mode output, provide a str

    # text mode input, returns a str
    # abc
    # (empty line)
    print(open('temp', 'r').read())

    # binary mode input, returns bytes
    print(open('temp', 'rb').read())  # b'abc\n'
    print('')

    # write and read a binary file
    open('temp', 'wb').write(b'abc\n')  # binary mode output, provide bytes

    # text mode input, returns a str
    # abc
    # (empty line)
    print(open('temp', 'r').read())

    # binary mode input, returns bytes
    print(open('temp', 'rb').read())  # b'abc\n'
    print('')

    # write and read truly binary data
    open('temp', 'wb').write(b'a\x00c')  # provide bytes

    print(open('temp', 'r').read())  # ac... returns a str
    print(open('temp', 'rb').read())  # b'a\x00c' returns bytes
    print('')

    BA = bytearray(b'\x41\x42\x43')
    open('temp', 'wb').write(BA)

    print(open('temp', 'r').read())  # ABC
    print(open('temp', 'rb').read())  # b'ABC'
    print('')
