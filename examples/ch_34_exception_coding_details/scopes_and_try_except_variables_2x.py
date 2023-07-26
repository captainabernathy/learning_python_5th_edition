if __name__ == '__main__':
    print 'code snippets from page 1147\n'

    try:
        1 / 0
    except Exception as X:  # 2.X does not localize X, so...
        print X  # integer division or modulo by zero
    print ''

    # X is available outside of the try block
    print X  # integer division or modulo by zero
    print ''

    # this is also true in 2.X when using the 3.X style as or the comman syntax
    try:
        1 / 0
    except Exception, X:
        print X  # integer division or modulo by zero
    print ''

    # so x is still available
    print X  # integer division or modulo by zero
    print ''
