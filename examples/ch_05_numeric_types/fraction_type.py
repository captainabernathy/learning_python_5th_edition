from fractions import Fraction
import decimal
from decimal import Decimal

if __name__ == '__main__':
    print('code snippets from pages 165-168\n')
    x = Fraction(1, 3)
    y = Fraction(4, 6)
    print(x)  # 1/3
    print(y)  # 2//3... reduces automatically
    print(x + y)  # 1
    print(x - y)  # -1/3
    print(x * y)  # 2/9
    print(Fraction('.25'))  # 1/4
    print(Fraction('1.25'))  # 5/4
    print(Fraction('.25') + Fraction('1.25'))  # 3/2
    print('')

    a = 1/3.0
    b = 4/6.0
    print(a)  # 0.33...3
    print(b)  # 0.66...6
    print(a + b)  # 1.0
    print(a - b)  # -0.33...3
    print(a * b)  # 0.22...2

    print(0.1 + 0.1 + 0.1 - 0.3)  # not 0.0
    # this is 0
    print(Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10)
          - Fraction(3, 10))
    # this is 0.0
    print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))

    print(1/3)  # 0.33...3
    print(Fraction(1, 3))  # 1/3

    decimal.getcontext().prec = 2  # set decimal precision
    print(Decimal(1) / Decimal(3))  # 0.33
    print((1/3) + (6/12))  # 0.833...3
    print(Fraction(6, 12))  # 1/2
    print(Fraction(1, 3) + Fraction(6, 12))  # 5/6
    print(Decimal(str(1/3)) + Decimal(str(6/12)))  # 0.83
    print(1000.0/1234567890)
    print(Fraction(1000, 1234567890))  # 100/123456789
    print('')

    # Fraction conversions and mixed types
    print((2.5).as_integer_ratio())  # (5, 2)

    f = 2.5
    z = Fraction(*f.as_integer_ratio())  # unpack and convert float to Fraction
    print(z)  # 5/2
    print(x + z)  # 17/6
    print(float(x))  # 0.33...3  convert a Fraction to a float
    print(float(z))  # 2.5
    print(float(x + z))  # 2.833...35
    print(17 / 6)  # 2.833....35

    # convert float to Fraction
    print(Fraction.from_float(1.75))  # 7/4
    # unpack and convert float to Fraction
    print(Fraction(*(1.75).as_integer_ratio()))  # 7/4

    print(x + 2)  # 7/3... Fraction + int -> Fraction
    print(x + 2.)  # 2.333...35 Fraaction + float -> float
    print(x + (1./3))  # 0.66...6 Fraction + float -> float
    print(x + (4./3))  # 1.66...65 Fraction + float -> float
    print(x + Fraction(4, 3))  # 5/3 Fraction + Fraction -> Fraction

    print(4.0 / 3)
    print((4.0/3).as_integer_ratio())  # (big1, big2) precision loss from float

    # unpack and convert float to Fraction
    a = x + Fraction(*(4.0/3).as_integer_ratio())
    print(a)  # 22517998136852479/13510798882111488
    print(22517998136852479/13510798882111488)  # 1.666... close to 5/3

    print(a.limit_denominator(10))  # 5/3... simplify to closest fraction
