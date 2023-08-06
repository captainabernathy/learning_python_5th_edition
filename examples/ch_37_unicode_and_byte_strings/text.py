# -*- coding: latin-1 -*-

# usage: python3 text.py

# any of the following string literal forms work in latin-1...
# changing the encoding above to either ascii or utf-8 fails bc the 0xC4
# and 0xE8 in my_str1 are not valid in either
import sys


if __name__ == '__main__':
    print('code snippets from pages 1228-1229\n')

    # my_str1 = 'AÄBèC'  # doesn't work as expected
    my_str2 = 'A\u00c4B\U000000e8C'
    my_str3 = 'A' + chr(0xC4) + 'B' + chr(0xE8) + 'C'

    print('Default encoding:', sys.getdefaultencoding())  # utf-8
    print('')

    # for astr in (my_str1, my_str2, my_str3):
    for astr in (my_str2, my_str3):
        print('{0}, strlen={1}, '.format(astr, len(astr)), end='')

        bytes1 = astr.encode()  # default utf-8... 2 bytes for non-ascii
        bytes2 = astr.encode('latin-1')  # one byte per char

        # bytes3 = astr.encode('ascii')  # ascii fails outised of 0-127

        print('byteslen1={0}, byteslen2={1}'.format(len(bytes1), len(bytes2)))
