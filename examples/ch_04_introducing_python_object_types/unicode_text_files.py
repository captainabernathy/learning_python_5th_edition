if __name__ == '__main__':
    print('code snippets from pages 127-128\n')
    S = 'sp\xc4m'
    print(S)  # spAm... A has an umlaut
    print(S[2])  # A with an umlaut

    # open/create a utf-8 encoded file for writing
    f = open('unidata.txt', 'w', encoding='utf-8')
    f.write(S)
    f.close()

    # open and decode a utf-8 encode file for reading
    text = open('unidata.txt', encoding='utf-8').read()  # auto-close
    print(text)
    print(len(text))  # 4... character code points

    # open/create a binary file for reading
    raw = open('unidata.txt', 'rb').read()
    print(raw)  # raw bytes
    print(len(raw))  # 5... bytes in UTF-8

    # specify encoding of raw data with the encode() method
    print(text.encode('utf-8'))  # a 5-character byte-string

    # use the decode() method to decode an encoded data object
    print(raw.decode('utf-8'))  # spAm... A w/umlaut

    # playing with different encoding
    print(text.encode('latin-1'))  # a 4-character byte-string
    print(text.encode('utf-16'))  # a 10-character byte-string
    print(len(text.encode('latin-1')), len(text.encode('utf-16')))  # 4 10

    # decode a literal
    print(b'\xff\xfes\x00p\x00\xc4\x00m\x00'.decode('utf-16'))
