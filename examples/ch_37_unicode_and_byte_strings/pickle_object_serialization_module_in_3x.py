import pickle


if __name__ == '__main__':
    print('code snippets from pages 1250-1252\n')

    # NOTE: pickle.dumps() returns a a pickle string... which is a bytes object
    # b'\x80\x04\x95\x0b\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03e.'
    print(pickle.dumps([1, 2, 3]))
    print('')

    # NOTE: protocol 0 => ASCII... but still bytes
    # default is protocol 3 => binary
    print(pickle.dumps([1, 2, 3], protocol=0))  # b'(lp0\nI1\naI2\naI3\na.'
    print('')

    try:
        pickle.dump([1, 2, 3], open('temp', 'w'))  # OK in 2X
    except TypeError as ex:
        print(ex)  # write() argument must be str, not bytes... in 3X
    print('')

    try:
        pickle.dump([1, 2, 3], open('temp', 'w'), protocol=0)  # error!
    except TypeError as ex:
        print(ex)  # write() argument must be str, not bytes... in 3X
    print('')

    pickle.dump([1, 2, 3], open('temp', 'wb'))  # always use binary in 3X

    # 3x... same as ^^^
    try:
        print(open('temp', 'r').read())
    except UnicodeDecodeError as ex:
        print(ex)  # 'utf-8' codec can't decode byte 0x80 in position 0:
                   # invalid start byte... in 3X
    print('')

    pickle.dump([1, 2, 3], open('temp', 'wb'))
    print(pickle.load(open('temp', 'rb')))  # [1,2,3]
    print('')

    # b'\x80\x04\x95\x0b\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03e.'
    print(open('temp', 'rb').read())
    print('')

    # version neutral
    pickle.dump([1, 2, 3], open('temp', 'wb'))

    print(pickle.load(open('temp', 'rb')))  # [1,2,3]
    print('')

