# usage: python3 mixing_string_types.py

if __name__ == '__main__':
    print('code snippets from pages 1232-1233\n')

    # NOTE: you must pass excpected types to functions
    B = b'spam'

    try:
        print(B.replace('pa', 'XY'))  # strings cause exception
    except TypeError as ex:
        print(ex)  # a bytes-like object is required, not 'str'
    print('')

    print(B.replace(b'pa', b'XY'))  # b'sXYm'
    print('')

    B = B'spam'  # not plain bytes
    
    try:
        print(bytes('pa'), bytes('xy'))  # missing encoding
    except TypeError as ex:
        print(ex)  # string argument without an encoding
    print('')

    print(B.replace(bytes('pa', 'ascii'), bytes('xy', 'utf-8')))  # b'sxym'
    print('')

    try:
        print(b'ca' + 'cd')  # error!
    except TypeError as ex:
        print(ex)  # can't concatenate bytes to str
    print('')

    print(b'ab'.decode() + 'cd')  # abcd... decode bytes to string
    print('')

    print(b'ab' + 'cd'.encode())  # b'abcd'... encode string to bytes
    print('')

    print(b'ab' + bytes('cd', 'ascii'))  # b'abcd'... ok
    print('')
