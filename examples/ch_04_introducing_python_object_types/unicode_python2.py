import codecs  # required by python 2

# NOTE: in Python 2.x Unicode strings are coded and displayed with a leading
# 'u', byte strings don't require or display with a leading 'b', and Unicode
# text files must be opened with codecs.open(), which accepts and encoding name

if __name__ == '__main__':
    print('code snippets from page 129\n')
    # open a unicode file for reading with codecs.open()
    # spAm... A w/umlaut
    print(codecs.open('unidata.txt', encoding='utf8').read())

    # 2.X read raw bytes
    print(open('unidata.txt', 'rb').read())  # spAm... A w/umlaut

    # 2.X read raw/undecoded data
    print(open('unidata.txt').read())  # spAm... A w/umlaut
