if __name__ == '__main__':
    print('code snippets from pages 108-110\n')
    # 3.X normal str strings are Unicode text
    print('sp\xc4m')  # A has umlat

    # byte strings are byte based data
    print(b'a\x01c')  # prints byte literal as b'a\x01c

    # 2.X Unicode literal works in 3.3+
    print(u'sp\u00c4m')  # A has umlat

    # 2.X Unicode strings are a distinct type
    print(u'sp\xc4m')  # A has umlat

    # normal str strings contain byte-based text/data
    print('a\x01c')  # prints ac but contains unicode character
    print(len('a\x01c'))  # 3

    # 3.X byte literal works in 2.6+
    print(b'a\x01c')  # prints byte literal

    # encoded to 4 bytes in UTF-8
    print('spam'.encode('utf8'))  # b'spam'

    # encoded to 10 bytes in UTF-16
    print('spam'.encode('utf16'))

    print('sp\xc4\u00c4\U000000c4m')  # three A-s with umlats

    print('\u00A3')  # lira sign
    print('\u00A3'.encode('latin1'))  # prints byte literal
    print(b'\xA3'.decode('latin1'))  # lira sign

    # NOTE: python 3 never allows normal and byte strings to mix without
    # explicit conversion
    # print(u'x' + b'y') # works in 2.X
    print(u'x' + 'y')  # ok

    print('x' + b'y'.decode())  # ok... decode bytes to string 'y'
    print('x'.encode() + b'y')  # ok... encode string x to bytes
