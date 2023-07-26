# NOTE: Exception classes simplify the process of passing along extra state
# information in an exception
class FormatError1(Exception):
    def __init__(self, line, file):
        self.line = line
        self.file = file


def parser1():
    # uses exception class
    raise FormatError1(42, file='spam.txt')


class FormatError2(Exception):
    pass


def parser2():
    raise FormatError2(42, 'spam.txt')


if __name__ == '__main__':
    print('code snippets from page 1175\n')

    try:
        parser1()
    except FormatError1 as ex:
        print('Error at: %s %s' % (ex.file, ex.line))  # spam.txt 42
    print('')

    try:
        parser2()
    except FormatError2 as ex:
        print('Error at:', ex.args[0], ex.args[1])  # 42 spam.txt
    print('')
