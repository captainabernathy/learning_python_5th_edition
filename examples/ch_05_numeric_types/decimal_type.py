import decimal
from decimal import Decimal

if __name__ == '__main__':
    print('code snippets from pages 163-164\n')
    print(0.1 + 0.1 + 0.1 - 0.3)  # not 0.0 bc floating-point arithmetic

    # NOTE: pass strings to Decimal to get expected result
    # 0.0
    print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))

    # 0.00
    print(Decimal('0.1') + Decimal('0.10') + Decimal('0.10') - Decimal('0.30'))

    # this won't be zero bc floating points used directly instead of strings
    print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3))
    # this will be 0
    print(Decimal(str(0.1)) + Decimal(str(0.1)) + Decimal(str(0.1))
          - Decimal(str(0.3)))
    print('')

    print(Decimal(1) / Decimal(7))  # a long decimal
    print(decimal.getcontext())  # all sorts of properties
    print(decimal.getcontext().prec)  # 28

    decimal.getcontext().prec = 4  # set precision to 4
    print(Decimal(1) / Decimal(7))  # 0.1429
    # 1.110E-17... closer to zero than before
    print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3))
    print('')

    print(1999 + 1.33)  # 2000.33
    decimal.getcontext().prec = 2
    pay = decimal.Decimal(str(1999 + 1.33))
    print(pay)  # 2000.33
