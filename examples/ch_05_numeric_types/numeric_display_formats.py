# usage: python3 numeric_display_formats.py

if __name__ == '__main__':
    print('code snippets from page 148\n')

    print(1 / 2.0)  # 0.5

    num = 1 / 3.0
    print(num)  # 0.333...

    # string formatting expression
    print('%e' % num)  # 3.333333e-01

    # alternative floating-point format
    print('%4.2f' % num)  # 0.33

    # string format method
    print('{0:4.2f}'.format(num))  # 0.33
