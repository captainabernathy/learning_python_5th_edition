# usage: python3 bytes_objects_method_calls.py

if __name__ == '__main__':
    print('code snippets from pages 1230-1231\n')

    # attributes in string but not in bytes
    # {'isprintable','format','casefold','format_map','isnumeric','encode',
    #  'isidentifier','isdecima'}
    print(set(dir('abc')) - set(dir(b'abc')))
    print('')

    # attributes in bytes but not in strings
    # {'fromhex','decode','hex'}
    print(set(dir(b'abc')) - set(dir('abc')))
    print('')

    # NOTE: bytes objects require bytes objects!
    B = b'spam'  # bytes literal
    print(B.find(b'pa'))  # 1
    print('')

    print(B.replace(b'pa', b'XY'))  # b'sXYm'... must use bytes arguments
    print('')

    print(B.split(b'pa'))  # [b's', b'm']
    print('')

    print(B)  # b'spam'
    print('')

    # NOTE: bytes are immutable
    try:
        B[0] = b'x'  # error!
        print(B)
    except TypeError as ex:
        print(ex)  # 'bytes' object does not support item assignment
    print('')

    # NOTE: string formatting only works on str objects!!!
    print('%s' % 99)  # 99
    print('')

    try:
        print(b'%s' % 99)  # error!
    except TypeError as ex:
        print(ex)  # %b requires a bites-like object, or an object that
                   # implements __bytes__, not 'int'
    print('')

    print('{0}'.format(99))  # 99
    print('')

    try:
        print(b'{0}'.format(99))  # error!
    except AttributeError as ex:
        print(ex)  # 'bytes' object has not attribute 'format'
    print('')
