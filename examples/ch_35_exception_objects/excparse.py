# usage: python(2/3) excparse.py

from __future__ import print_function


# NOTE: an Exception class can also provide methodos that can be called by a
# handler
class FormatError(Exception):
    logfile = 'formaterror.txt'

    def __init__(self, line, file):
        self.line = line
        self.file = file

    def logerror(self):
        log = open(self.logfile, 'a')
        print('Error at:', self.file, self.line, file=log)


def parser():
    raise FormatError(40, 'spam.txt')


if __name__ == '__main__':
    print('code snippets from page 1176\n')

    try:
        parser()
    except FormatError as ex:
        ex.logerror()  # calls ex's logerror() method
