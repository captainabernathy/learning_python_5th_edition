import math
import random

if __name__ == '__main__':
    print('code snippets from pages 160-162\n')
    print(math.pi, math.e)  # constants
    print(math.sin(2 * math.pi / 180))  # trig functions
    print(math.sqrt(144), math.sqrt(2))  # square root
    print(pow(2, 4), 2 ** 4, 2.0 ** 4)  # exponentiation
    print(abs(-42.0), sum((1, 2, 3, 4)))  # absolute value, summation
    print(min(3, 1, 2, 4), max(3, 1, 2, 4))  # min, max
    print('')

    print(math.floor(2.567), math.floor(-2.567))  # floor() rounds down
    print(math.trunc(2.567), math.trunc(-2.567))  # trunc() drops decimal part
    print(int(2.567), int(-2.567))  # truncate and convert to int
    print(round(2.567), round(2.467), round(2.567, 2))  # 3, 2, 2.57
    print('')

    print('%.1f' % 2.567, '{0:.2f}'.format(2.567))  # 2.6, 2.57
    # 0.333...3 0.33 0.33
    print(1 / 3.0, round(1 / 3.0, 2), '%.2f' % (1 / 3.0))
    print('')

    print(math.sqrt(144))  # 12.0
    print(144 ** .5)  # 12.0
    print(pow(144, .5))  # 12.0

    print(math.sqrt(1234567890))
    print(1234567890 ** .5)
    print(pow(1234567890, .5))
    print('')

    print(random.random())  # random number b/t 0-1
    print(random.random())
    print(random.randint(1, 10))  # random int between 1,10 inclusive
    print(random.randint(1, 10))
    print('')

    # random selection from a list
    print(random.choice(['Life of Brian', 'Holy Grail', 'Meaning of Life']))
    print(random.choice(['Life of Brian', 'Holy Grail', 'Meaning of Life']))

    suits = ['hearts', 'clubs', 'diamonds', 'spades']
    print(suits)
    random.shuffle(suits)  # shuffle list
    print(suits)
    random.shuffle(suits)  # shuffle list again
    print(suits)
    random.shuffle(suits)  # shuffle list again
    print(suits)
