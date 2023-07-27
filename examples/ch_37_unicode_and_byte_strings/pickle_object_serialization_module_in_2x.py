import pickle

if __name__ == '__main__':
    print 'code snippets from pages 1251-1252\n'

    # (lp0
    # I1
    # aI2
    # aI3
    # a.
    print pickle.dumps([1, 2, 3])
    print ''

    # ]q(KKKe.
    print pickle.dumps([1, 2, 3], protocol=1)
    print ''

    try:
        pickle.dump([1, 2, 3], open('temp', 'w'))  # ok in 2X
    except TypeError as ex:
        print ex  # write() argument must be str, not bytes... 3X
    print ''

    try:
        print pickle.load(open('temp'))  # [1,2,3]... ok in 2X
    except TypeError as ex:
        print ex  # a bytes-like object is required, not 'str'... in 3X
    print ''

    pickle.dump([1, 2, 3], open('temp', 'wb'))  # always use binary in 3X

    # 3x... same as ^^^
    try:
        # (lp0
        # I1
        # aI2
        # aI3
        # a.
        print open('temp').read()  # ok in 2X
    except UnicodeDecodeError as ex:
        print ex  # 'utf-8' codec can't decode byte 0x80 in position 0:
                  # invalid start byte
    print ''

    # version neutral
    pickle.dump([1, 2, 3], open('temp', 'wb'))

    print(pickle.load(open('temp', 'rb')))  # [1,2,3]
    print('')


