# usage: python3 byte_string_literals_encoded_text.py

if __name__ == '__main__':
    print('code snippets from pages 1123-1124\n')

    # NOTE: bytes must be decoded to str to print their non-ASCII characters
    S = 'A\xC4B\xE8C'  # A non-ascii B non-ascii C
    print(S)  # AÄBèC
    print('')

    S = 'A\u00C4B\U000000E8C'
    print(S)  # AÄBèC
    print('')

    B = b'A\xC4B\xE8C'  # NOTE: byte recognizes hex but not unicode
    print(B)  # b'A\xc4B\xe8C'
    print('')

    # NOTE: escape sequences silently taken as literals... not as escapes!!!
    B = b'A\u00C4B\U000000E8C'
    print(B)  # b'A\\u00C4B\\U000000e8C'
    print(len(B))  # 19
    print('')

    # NOTE: chars must be ascii or escapes
    B = b'A\xC4B\xE8C'  # byte recognizes hex but not unicode...
    print(B)  # b'A\xc4B\xe8C'... prints non-ascii as hex
    print(B.decode('latin-1'))  # AÄBèC... decode to latin-1 to print as text
    print('')

    print(S.encode())  # b'A\xc3\x84B\xc3\xa8C'... default encode to utf-8
    print(S.encode('utf-8'))  # b'A\xc3\x84B\xc3\xa8C'... same as ^^^
    print('')

    try:
        print(B.decode())  # raw bytes cannot be converted to utf-8
    except UnicodeDecodeError as ex:
        print(ex)  # 'utf-8' codec can't decode byte 0xc4 in position 1:
                   # invalid continuation byte
    print('')
