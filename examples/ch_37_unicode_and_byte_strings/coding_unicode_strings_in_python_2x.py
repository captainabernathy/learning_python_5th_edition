# NOTE: run with python2

if __name__ == '__main__':
    print 'code snippets from pages 1225-1227\n'

    S = 'A\xC4B\xE8C'  # string of 8-bit bytes
    print S  # non-printable characters show up as garbage
    print ''

    U = S.decode('latin1')  # decode bytes to unicode per latin-1
    print U  # no garbage
    print ''

    try:
        print S.decode('utf-8')  # encoded form not compatible with utf8
    except UnicodeDecodeError as ex:
        print ex  # 'utf-8' codec can't decode byte 0xc4 in position 1:
                  # invalid continuation byte
    print ''

    try:
        print S.decode('ascii')  # encoded bytes beyond ascii range
    except UnicodeDecodeError as ex:
        print ex  # 'ascii' codec can't decode byte 0xc4 in position 1:
                  # ordinal not in range(128)
    print ''

    # to code unicode text make a unicode object with u'xxx'
    U = u'A\xC4B\xE8C'
    print U
    print ''

    print U.encode('latin1')  # non-printable characters show up as garbage
    print U.encode('utf-8')  # no garbage
    print ''

    U = u'A\xC4B\xE8C'  # hex escapes for non-ascii
    print U  # no garbage

    U = u'A\u00C4B\U000000E8C'  # unicode escapes for non-ascii
    print U  # no garbage
    print ''

    S = 'A\xC4B\xE8C'  # hex escapes work...
    print S  # but may print oddly... non-printable chars show up as garbage

    print S.decode('latin-1')  # ok... no garbage
    print ''

    # NOTE: non-unicode escapes are taken literally!!!
    S = 'A\u00C4B\U000000EBC'
    print S  # A\u00C4B\U000000EBC
    print len(S)  # 19
    print ''
