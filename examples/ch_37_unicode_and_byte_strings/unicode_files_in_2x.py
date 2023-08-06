# usage: python2 unicode_files_in_2x.py

import codecs

if __name__ == '__main__':
    print 'code snippets from page 1245\n'

    # NOTE: in 2X, use unicode() where you would use str() in 3X, and use
    # codecs.open where you would use open() in 3X

    S = u'A\xc4B\xe8C'

    print S

    print len(S)
    print ''

    print S.encode('latin-1')

    print S.encode('utf-8')
    print ''

    # NOTE: writes encode
    codecs.open('latindata', 'w', encoding='latin-1').write(S)
    codecs.open('utfdata', 'w', encoding='utf-8').write(S)

    print open('latindata', 'rb').read()
    print open('utfdata', 'rb').read()
    print ''

    # NOTE: reads decode
    print codecs.open('latindata', 'r', encoding='latin-1').read()
    print codecs.open('utfdata', 'r', encoding='utf-8').read()
