# usage: python3 character_encoding_schemes.py

if __name__ == '__main__':
    print('code snippets from pages 1208-1209\n')

    # ord() returns a unicode code point for a one-character string
    print(ord('a'))  # 97
    print(hex(97))  # 0x61... hexadecimal representation of integer
    print(chr(97))  # a... returns a single character unicode string
    print('')

    # beyond ascii
    print(0xC4)  # 196
    print(chr(0xC4))  # Ä... A with trema
    print('')

    S = 'ni'
    # NOTE: a string's encode() method returns a byte-string encoded with the
    # given scheme
    print(S.encode('ascii'))  # b'ni'
    print(S.encode('latin1'))  # b'ni'
    print(S.encode('utf8'))  # b'ni'
    print('')  # each of ^^^ are the same

    # b'\xff\xfen\x00i\x00' 6
    print(S.encode('utf16'), len(S.encode('utf16')))

    # b'\xff\xfe\x00\x00n\x00\x00\x00i\x00\x00\x00' 12
    print(S.encode('utf32'), len(S.encode('utf32')))
