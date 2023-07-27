if __name__ == '__main__':
    print('code snippets from pages 1222-1223\n')

    S = 'A\u00c4B\U000000e8C'  # A non-ascii B non-ascii C
    print(S)  # AÄBèC
    print(len(S))  # 5
    print('')

    print(S.encode('latin-1'))  # b'A\xc4B\xe8C'
    print(len(S.encode('latin-1')))  # 5 in latin-1
    print('')

    print(S.encode('utf-8'))  # b'A\xc3\x84B\xc3\xa8C'
    print(len(S.encode('utf-8')))  # 7 in utf-8
    print('')

    # build up unicode strings piecemeal using chr()
    S = 'A' + chr(0xC4) + 'B' + chr(0xE8) + 'C'
    print(S)  # AÄBèC
    print(len(S))  # 5
    print('')

    # some Western European encodings
    print(S.encode('cp500'))  # b'\xc1c\xc2T\xc3'
    print(S.encode('cp850'))  # b'A\x8eB\x8aC'
    print('')

    S = 'spam'
    print(S.encode('latin-1'))  # b'spam'
    print(S.encode('utf-8'))  # b'spam' same as latin 1
    print(S.encode('cp500'))  # b'\xa2\x97\x81\x94'
    print(S.encode('cp850'))  # b'spam' same as utf-8 and latin-1
    print('')

    S = 'A\u00c4B\U000000e8C'  # A non-ascii B non-ascii C
    print(S.encode('utf-16'))  # 'b\xff\xfeA\x00\xc4\x00B\x00\xe8\x00C\x00'
    print(len(S.encode('utf-16')))  # 12
    print('')

    S = 'spam'
    print(S.encode('utf-16'))  # 'b\xff\xfes\x00p\x00a\x00m\x00'
    print(len(S.encode('utf-16')))  # 10
    # b'\xff\xfe\x00\x00s\x00\x00\x00p\x00\x00\x00a\x00\x00\x00m\x00\x00\x00'
    print(S.encode('utf-32'))
    print(len(S.encode('utf-32')))  # 20
    print('')
