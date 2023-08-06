# usage: python3 coding_ascii_text.py

if __name__ == '__main__':
    print('code snippets from page 1219\n')

    print(ord('X'))  # 88... get the unicode code point
    print(chr(88))  # X... get the character at point 88
    print('')

    S = 'XYZ'  # a unicode string of ascii text
    print(S)  # XYZ
    print(len(S))  # 3
    print([ord(c) for c in S])  # [88,89,90]
    print('')

    # they are all the same (b'XYX')
    print(S.encode('ascii'))  # b'XYZ'
    print(S.encode('latin-1'))  # b'XYZ'
    print(S.encode('utf-8'))  # b'XYZ'
    print('')

    # the byte objects returned by encoding ascii this way are sequences of
    # short integers
    print(S.encode('latin-1'))  # b'XYZ'
    print(S.encode('latin-1')[0])  # 88
    print(list(S.encode('latin-1')))  # [88,89,90]
    print('')
