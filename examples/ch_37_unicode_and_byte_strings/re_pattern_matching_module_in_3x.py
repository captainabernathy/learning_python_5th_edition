import re


if __name__ == '__main__':
    print('code snippets from pages 1247-1248\n')

    S = 'Bugger all down here on earth!'  # line of text

    # NOTE: in 3X, use bytes for non-ascii text
    B = b'Bugger all down here on earth!'  # a line of bytes

    # match line to pattern
    # ('Bugger all', 'here', 'earth!')
    print(re.match('(.*) down (.*) on (.*)', S).groups())
    print('')

    # match bytes substrings
    # (b'Bugger all', b'here', b'earth!')
    print(re.match(b'(.*) down (.*) on (.*)', B).groups())
    print('')

    # NOTE: you can't use string pattern to match on a bytes object
    try:
        print(re.match('(.*) down (.*) on (.*)', B).groups())
    except TypeError as ex:
        print(ex)  # cannot use a string pattern on a bytes-like object
    print('')

    # NOTE: you can't use bytes pattern to match on a string object
    try:
        print(re.match(b'(.*) down (.*) on (.*)', S).groups())
    except TypeError as ex:
        print(ex)  # cannot use bytes pattern on a string-like object
    print('')

    # (b'Bugger all', b'here', b'earth!')
    print(re.match(b'(.*) down (.*) on (.*)', bytearray(B)).groups())  # OK
    print('')

    # NOTE: you can't use string pattern on bytes-like object
    try:
        print(re.match('(.*) down (.*) on (.*)', bytearray(B)).groups())
    except TypeError as ex:
        print(ex)  # canot use string patter on bytes-like object
    print('')
