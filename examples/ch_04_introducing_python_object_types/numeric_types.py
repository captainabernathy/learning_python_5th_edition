import math
import random

if __name__ == '__main__':
    print('code snippets from pages 99-101\n')

    # integer addition
    print(123 + 222)  # 345

    # floating-point multiplication
    print(1.5 * 4)  # 6.0

    # 2 to the 100
    print(2 ** 100)  # a really big number

    # how many digits in 2 ** 1M
    print(len(str(2 ** 1000000)))  # 301030

    # pi from math module
    print(math.pi)  # pi to several places

    # square root of 85
    print(math.sqrt(85))  # 9.21954...

    # random number b/t 0 and 1 via random module's random() function
    print(random.random())

    # random selection via random module's choice() function
    print(random.choice([1, 2, 3, 4]))
