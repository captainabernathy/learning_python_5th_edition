# usage: python3 formats_currency.py

from __future__ import print_function  # for 2.X compatibility
from formats import money

if __name__ == '__main__':
    print('code snippets from pages 778-777\n')

    X = 54321.987

    print(money(X), money(X, 0, ''))

    # NOTE: for compatibility with python 2.X, prepend unicode and hex escape
    # sequences with 'u' in python3 >= 3.3
    print(money(X, currency=u'\xA3'), money(X, currency=u'\u00A5'))

    # NOTE: for compatibility with python 3.X use a leading 'b' to encode raw
    # byte string literas in python 2.X
    print(money(X, currency=b'\xA3'.decode('latin-1')))

    print(money(X, currency=u'\u20AC'),
          money(X, 0, b'\xA4'.decode('iso-8859-15')))

    print(money(X, currency=b'\xA4'.decode('latin-1')))

    print(u'\xA5' + '1', '%s2' % u'\u00A3')
