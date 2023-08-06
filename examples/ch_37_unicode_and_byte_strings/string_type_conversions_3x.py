# usage: python3 string_type_conversions_3x.py

import locale
import sys


if __name__ == '__main__':
    print('code snippets from page 1218\n')

    S = 'eggs'
    print(S.encode())  # b'eggs'... str->bytes: encode text into raw bytes
    print(bytes(S, encoding='ascii'))  # b'eggs'... str->bytes (alternative)
    print('')

    B = b'spam'
    print(B.decode())  # spam... bytes->str: decode raw bytes into text
    print(str(B, encoding='ascii'))  # spam... bytes->str (alternative)
    print('')

    print(sys.platform)  # linux
    # UTF-8 utf-8
    print(locale.getpreferredencoding(False), sys.getdefaultencoding())
    print('')

    try:
        print(bytes(S))  # error... bytes requires encoding
    except TypeError as ex:
        print(ex)  # string argument without an encoding
    print('')

    print(str(B))  # b'spam'... encoding optional

    # NOTE: a str() call without an encoding returns the object's print
    # string... NOT its string converted form
    print(B)  # b'spam'
    print(len(str(B)))  # 7... length of "b'spam'"
    print(len(str(B, encoding='ascii')))  # 4
    print('')
