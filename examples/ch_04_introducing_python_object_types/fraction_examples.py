# NOTE: fractions are rational numbers with both a numerator and a denominator

from fractions import Fraction

if __name__ == '__main__':
    print('code snippets from page 130\n')
    f = Fraction(2, 3)
    print(f)  # 2/3
    print(f + 1)  # 5/3

    print(f + Fraction(1, 2))  # 7/6
