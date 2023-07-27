import sys

if __name__ == '__main__':
    print('code snippets from pages 1243-1245\n')

    S = 'spam\nSPAM\n'

    print(open('temp.txt', 'w', encoding='utf-8').write(S))  # 10
    print('')

    print(open('temp.txt', 'rb').read())  # b'spam\nSPAM\n'... no BOM
    print('')

    # NOTE: in UTF-8, the more specific encoding 'utf-8-sig' forces Python to
    # both skip and write a BOM on input and output, respectively... HOWEVER,
    # the more general 'utf-8' does NOT
    print(open('temp.txt', 'w', encoding='utf-8-sig').write(S))
    print('')

    # b'\xef\xbb\xbfspam\nSPAM\n'
    print(open('temp.txt', 'rb').read())  # wrote BOM
    print('')

    # spam
    # SPAM
    # (empty line)
    print(open('temp.txt', 'r').read())

    # spam
    # SPAM
    # (empty line)
    print(open('temp.txt', 'r', encoding='utf-8-sig').read())

    print(open('temp.txt', 'w').write(S))  # 10
    print('')

    print(open('temp.txt', 'rb').read())  # b'spam\nSPAM\n'
    print('')

    # spam
    # SPAM
    # (empty line)
    print(open('temp.txt', 'r').read())

    # spam
    # SPAM
    # (empty line)
    print(open('temp.txt', 'r', encoding='utf-8').read())

    # spam
    # SPAM
    # (empty line)
    print(open('temp.txt', 'r', encoding='utf-8-sig').read())

    print(sys.byteorder)  # little
    print('')

    print(open('temp.txt', 'w', encoding='utf-16').write(S))  # 10
    print('')

    # NOTE: in UTF-16, the BOM is always processed for 'utf-16'
    # b'\xff\xfes\x00p\x00a\x00m\x00\n\x00S\x00P\x00A\x00M\x00\n\x00'
    print(open('temp.txt', 'rb').read())
    print('')

    # spam
    # SPAM
    # (empty line)
    print(open('temp.txt', 'r', encoding='utf-16').read())

    S = '\ufeffspam\nSPAM\n'

    # NOTE: utf-16-be specifies big endian
    print(open('temp.txt', 'w', encoding='utf-16-be').write(S))  # 11
    print('')

    # b'\xfe\xff\x00s\x00p\x00a\x00m\x00\n\x00S\x00P\x00A\x00M\x00\n'
    print(open('temp.txt', 'rb').read())
    print('')

    # spam
    # SPAM
    # (empty line)
    print(open('temp.txt', 'r', encoding='utf-16').read())

    # spam
    # SPAM
    # (empty line)
    print(open('temp.txt', 'r', encoding='utf-16-be').read())

    # NOTE: utf-16-le specifices little endian
    print(open('temp.txt', 'w', encoding='utf-16-le').write('SPAM'))  # 4
    print('')

    print(open('temp.txt', 'rb').read())  # b'S\x00P\x00A\x00M\x00'
    print('')

    # NOTE: encoding utf-16-le must be specified when reading utf-16, little
    # endian encoded file
    print(open('temp.txt', 'r', encoding='utf-16-le').read())  # SPAM
    print('')

    try:
        # error.. requres 'utf-16-le'
        print(open('temp.txt', 'r', encoding='utf-16').read())
    except UnicodeError as ex:
        print(ex)  # UTF-16 stream does not start with BOM

