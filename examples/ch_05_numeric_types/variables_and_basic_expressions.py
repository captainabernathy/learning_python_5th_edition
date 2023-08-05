# usage: python3 variables_and_basic_expressions.py

if __name__ == '__main__':
    print('code snippets from pages 146-147\n')

    a = 3
    b = 4
    print(a + 1, a - 1)  # 4 2
    print(b * 3, b / 2)  # 12 2.0
    print(a % 2, b ** 2)  # 1 16
    print(a + 4.0, 2.0 ** b)  # 7.0 16.0
    print('')

    print(b / 2 + a)  # (b/2) + a... 5
    print(b / (2 + a))  # 0.8
