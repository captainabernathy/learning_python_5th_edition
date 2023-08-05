# usage: python3 unicode_strings.py
# coding=utf-8

if __name__ == '__main__':
    print('code snippets from pages 108-110\n')

    # 3.X normal str strings are Unicode text
    print('sp\xc4m')  # spÄm

    # byte strings are byte based data
    print(b'a\x01c')  # b'a\x01c

    # 2.X Unicode literal works in 3.3+
    print(u'sp\u00c4m')  # spÄm

    # 2.X Unicode strings are a distinct type
    print(u'sp\xc4m')  # spÄm

    # normal str strings contain byte-based text/data
    print('a\x01c')  # prints ac but contains unicode character
    print(len('a\x01c'))  # 3

    # 3.X byte literal works in 2.6+
    print(b'a\x01c')  # b'a\x01c'... byte literal

    # encoded to 4 bytes in UTF-8
    print('spam'.encode('utf8'))  # b'spam'

    # encoded to 10 bytes in UTF-16
    print('spam'.encode('utf16'))  # b'\xff\xfes\x00p\x00a\x00m\x00'

    print('sp\xc4\u00c4\U000000c4m')  # spÄÄÄm

    print('\u00A3')  # £
    print('\u00A3'.encode('latin1'))  # b'\xa3'
    print(b'\xA3'.decode('latin1'))  # £

    # NOTE: python 3 never allows normal and byte strings to mix without
    # explicit conversion
    # print(u'x' + b'y') # works in 2.X
    print(u'x' + 'y')  # xy... ok

    print('x' + b'y'.decode())  # xy... ok... decode bytes to string 'y'
    print('x'.encode() + b'y')  # b'xy... ok... encode string x to bytes
