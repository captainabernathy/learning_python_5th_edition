# usage: python3 convert_encoding.py

if __name__ == '__main__':
    print('code snippets from pages 1224-1225\n')

    # NOTE: it is necessary to provide an explicit encoding name to encode to
    # and decode from a string using a different encoding
    B = b'A\xc3\x84B\xc3\xa8C'  # A non-ascii B non-ascii C encoded in utf-8
    print(B)  # b'A\xc3\x84B\xc3\xa8C'
    print('')

    # S = B.decode()  # ok only bc B is utf-8 encoded
    S = B.decode('utf-8')
    print(S)  # AÄBèC
    print('')

    T = S.encode('cp500')  # convert to encoded bytes per EBCDIC
    print(T)  # b'\xc1c\xc2T\xc3'
    print('')

    U = T.decode('cp500')  # convert back to unicode per EBCDIC
    print(U)  # AÄBèC
    print('')

    print(U.encode())  # b'A\xc3\x84B\xc3\xa8C'... per default utf-8 encoding
    print('')
