# usage: python3 patternparse.py

import re

if __name__ == '__main__':
    print('code snippets from page 1253\n')

    text = open('mybooks.xml').read()

    # NOTE: the re module's findall() function returns a list of matches
    found = re.findall('<title>(.*)</title>', text)

    # Learning Python
    # Programming Python
    # Python Pocket Reference
    [print(title) for title in found]
    print('')
