# usage: python3 encoding_and_decoding_non_ascii_text.py

if __name__ == '__main__':
    print('code snippets from pages 1221-1222\n')

    S = '\u00c4\u00e8'  # utf-16
    print(S)  # Äè
    print(len(S))  # 2
    print('')

    try:
        print(S.encode('ascii'))  # S is beyond the ascii range
    except UnicodeEncodeError as ex:
        print(ex)  # 'ascii' code can't encode characters in positions 0-1:
                   # ordinal not in range(128)
    print('')

    print(S.encode('latin-1'))  # b'\xc4\xe8' 1-byte per character when encoded
    print(len(S.encode('latin-1')))  # 2
    print('')

    print(S.encode('utf-8'))  # b'\xc3\x84\xc3\xa8' 2 bytes per character
                              # when encoded
    print(len(S.encode('utf-8')))  # 4
    print('')

    # going the other way...
    B = b'\xc4\xe8'  # text encoded as latin-1
    print(B)  # b'xc4\xe8'
    print(len(B))  # 2
    print(B.decode('latin-1'))  # Äè
    print('')

    B = b'\xc3\x84\xc3\xa8'  # text encoded as utf-8
    print(B)  # b'\xc3\x84\xc3\xa8'
    print(len(B))  # 4
    print(B.decode('utf-8'))  # Äè
    print('')
