# usage: python2 re_pattern_matching_module_in_2x.py

import re

if __name__ == '__main__':
    print 'code snippets from page 1248\n'

    S = 'Bugger all down here on earth!'  # line of text

    # NOTE: in 2X, use unicode for non-ascii text
    U = u'Bugger all down here on earth!'  # a line of unicode text

    # match line to pattern
    # ('Bugger all', 'here', 'earth!')
    print re.match('(.*) down (.*) on (.*)', S).groups()
    print ''

    # match bytes substrings
    # (u'Bugger all', u'here', u'earth!')
    print re.match(b'(.*) down (.*) on (.*)', U).groups()
    print ''
