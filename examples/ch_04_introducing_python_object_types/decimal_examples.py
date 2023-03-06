import decimal  # provides for fixed precision floats

if __name__ == '__main__':
    print('code snippets from page 130\n')
    print(1 / 3)  # 0.333...
    print((2 / 3) + (1 / 2))  # 1.166...

    d = decimal.Decimal('3.141')
    print(d)  # 3.141
    print(d + 1)  # 4.141

    # set precision
    decimal.getcontext().prec = 2
    print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))  # 0.33
