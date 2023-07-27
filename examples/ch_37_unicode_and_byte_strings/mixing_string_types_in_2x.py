# NOTE: run with python2

if __name__ == '__main__':
    print 'code snippets from pages 1227-1228\n'

    # in python2 unicode and non-unicode str objects can be freely mixed in
    # expressions... as long as the str is compatible with the unicode object
    print u'ab' + 'cd'  # abcd

    # ^^^ only works if the 8-bit string happens to contain only 7-bit ascii
    # bytes
    S = 'A\xC4B\xE8C'
    U = u'A\xC4B\xE8C'
    try:
        print S + U
    except UnicodeDecodeError as ex:
        print ex  # 'ascii' codec can't decode byte 0xc4 in position 1:
                  # ordinal not in range(128)
    print ''

    print 'abc' + U  # can mix only if str is all 7-bit ascii
    print S.decode('latin-1') + U  #  manual conversion
    print ''

    print u'\xA3' + '999.99'
    print ''

    print str(u'spam')  # unicode to normal
    print unicode('spam')  # normal to unicode
