if __name__ == '__main__':
    print('code snippets from pages 1239-1240\n')

    print(open('temp', 'w').write('abc\n'))  # 4

    try:
        open('temp', 'w').write(b'abc\n')  # error! can't write bytes in text
                                           # mode
    except TypeError as ex:
        print(ex)  # write() argument must be str, not bytes
    print('')

    print(open('temp', 'wb').write(b'abc\n'))

    try:
        open('temp', 'wb').write('abc\n')  # error! can't write str in binary
                                           # mode
    except TypeError as ex:
        print(ex)  # a bytes-like object is required, not 'str'
    print('')

    print(chr(0xFF))  # ÿ... y w/trema
    print(chr(0xFE))  # þ... '\xfe'
    print('')

    try:
        open('temp', 'w').write(b'\xFF\xFE\xFD')  # error! must be a str
    except TypeError as ex:
        print(ex)  # write() argument must be str, not bytes
    print('')

    print(open('temp', 'w').write('\xFF\xFE\xFD'))  # ok bytes wrappend in str
    print(open('temp', 'wb').write(b'\xFF\xFE\xFD'))  # ok
    print('')

    # can always read binary bytes
    print(open('temp', 'rb').read())  # b'\xff\xfe\xfd'

    # possibly unable to read bytes as text unless decodable
    try:
        print(open('temp', 'r').read())  # error!
    except UnicodeDecodeError as ex:
        print(ex)  # 'utf-8' codec can't decode byte 0xff in position 0:
                   # invalid start byte
    print('')
