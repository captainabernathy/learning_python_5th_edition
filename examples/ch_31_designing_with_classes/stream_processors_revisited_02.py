# usage: python3 stream_processors_revisited_01.py

from converters import Uppercase


# provides a write() method that wraps a line of text in <PRE> </PRE>  tags
class HTMLize:
    def write(self, line):
        print('<PRE>%s</PRE>' % line.rstrip())


if __name__ == '__main__':
    print('code snippets from page 970\n')

    # reads the lines trispam.txt, wraps them in <PRE> </PRE> tags, and writes
    # them to stdout
    Uppercase(open('trispam.txt'), HTMLize()).process()
