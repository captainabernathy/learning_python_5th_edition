if __name__ == '__main__':
    print('code snippets from pages 1240-1242\n')

    S = 'A\xc4B\xe8C'  # 5-character decoded string, non-ascii
    print(S)  # AÄBèC
    print(len(S))  # 5
    print('')

    # Manual Encoding
    # encode a string to raw bytes according to the target encoding name
    L = S.encode('latin-1')
    print(L)  # b'A\xc4B\xe8\C'
    print(len(L))  # 5
    print('')

    U = S.encode('utf-8')
    print(U)  # b'A\xc3\x84B\xc3\xa8C'
    print(len(U))  # 7
    print('')

    # File Output Encoding
    # pass encoding name to open
    print(open('latindata', 'w', encoding='latin-1').write(S))  # 5
    print(open('utf8data', 'w', encoding='utf-8').write(S))  # 5
    print('')

    print(open('latindata', 'rb').read())  # b'A\xc4B\xe8C'... read raw bytes
    print(open('utf8data', 'rb').read())  # b'A\xc3\x84B\xc3\xa8C'
    print('')

    # File Input Decoding
    # pass file's encoding type to open

    # decoding automatically when read
    print(open('latindata', 'r', encoding='latin-1').read())  # AÄBèC
    print(open('utf8data', 'r', encoding='utf-8').read())  # AÄBèC
    print('')

    X = open('latindata', 'rb').read()  # manual decoding
    print(X.decode('latin-1'))  # AÄBèC

    X = open('utf8data', 'rb').read()

    # NOTE: utf-8 is default
    print(X.decode())  # AÄBèC...
    print('')
