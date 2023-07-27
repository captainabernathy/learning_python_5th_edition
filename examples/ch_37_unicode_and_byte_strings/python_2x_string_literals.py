# NOTE: run with python2

if __name__ == '__main__':
    print 'code snippets from page 1217\n'

    B = b'spam'  # just str in 2x
    S = 'eggs'  # str is a byte/character sequence

    print type(B), type(S)  # <type 'str'> <type 'str'>
    print B, S  # spam eggs
    print B[0], S[0]  # s e
    print list(B), list(S)  # ['s','p','a','m'] ['e','g','g','s']
    print ''

    U = u'spam'  # 2x unicode literal makes a distinct type
    print type(U)  # <type 'unicode'>
    print U  # spam
    print U[0]  # s
    print list(U)  # [u's',u'p',u'a',u'm']
    print ''
