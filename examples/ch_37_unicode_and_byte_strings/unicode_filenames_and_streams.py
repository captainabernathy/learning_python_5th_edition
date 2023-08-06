# usage: python3 unicode_filenames_and_streams.py

import sys
import glob

if __name__ == '__main__':
    print('code snippets from page 1246\n')

    print(sys.getdefaultencoding())  # utf-8
    print(sys.getfilesystemencoding())  # utf-8
    print('')

    # Filenames: Text versus bytes
    f = open('xxx\u00A5', 'w')  # non-ascii filename
    f.write('\xA5999\n')  # write 5 characters
    f.close()

    # ¥999
    # (empty line)
    print(open('xxx\u00A5').read())  # Text: auto-encoded

    # ¥999
    # (empty line)
    print(open('xxx\xA5').read())

    # ¥999
    # (empty line)
    print(open(b'xxx\xc2\xa5').read())  # Bytes: pre-encoded

    # use glob() for filename expansion (globbing)
    print(glob.glob('*\u00A5*'))  # ¥999... get decoded text for decoded text
    print('')

    # get encoded bytes for encoded bytes
    print(glob.glob(b'*\xA5*'))  # [b'xxx\xc2\xa5']
