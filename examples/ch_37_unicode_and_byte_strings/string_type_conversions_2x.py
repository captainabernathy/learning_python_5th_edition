# NOTE: run with python2

if __name__ == '__main__':
    print 'code snippets from page 1218\n'

    S, U = 'spam', u'eggs'
    print S  # spam
    print U  # eggs
    print ''

    # NOTE: conversions in 2X occur b/t encoded str and decoded unicode...
    # HOWEVER conversions occur in 3X b/t encoded bytes and decoded str

    # 2x converts str->uni, uni->str
    print unicode(S)  # spam... 2X unicode() converts a string to unicode
    print str(U)  # eggs... 2X str() converts unicode to string
    print ''

    # 3x converts byte->str, str->byte
    print S.decode()  # spam... 2X the decode() method converts a string
                      # to unicode
    print U.encode()  # eggs... 2X the encode() method unicode to string
