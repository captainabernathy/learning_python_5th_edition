# usage: python2 text_and_binary_modes_in_2x.py

from __future__ import print_function

if __name__ == '__main__':
    print('code snippets from page 1238\n')

    # in 2X there is not major distinction b/t text and binary files
    open('temp', 'w').write('abd\n')
    
    # abc
    # (empty line)
    print(open('temp', 'r').read())

    # abc
    # (empty line)
    print(open('temp', 'rb').read())
    print('')

    open('temp', 'wb').write('abc\n')

    # abc
    # (empty line)
    print(open('temp', 'r').read())

    # abc
    # (empty line)
    print(open('temp', 'rb').read())
