# usage: python3 formats_importer.py

from formats import money  # import money() function from formats by name
from formats import commas  # import commas() function from formats by name

if __name__ == '__main__':
    print('code snippets from pages 776-777\n')

    print(money(123.456))  # $123.46
    print(money(-9999999.99, 15))  # $  -9,999,999.99
    X = 99999999999999999999

    # 99,999,999,999,999,999,999 (99999999999999999999)
    print('%s (%s)' % (commas(X), X))
