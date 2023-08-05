# usage: python3 timer0_test.py
# program tests the timer() function from the timer0 module

from timer0 import timer

if __name__ == '__main__':
    print('code snippets from page 652\n')

    print(timer(pow, 2, 1000))
    print(timer(str.upper, 'spam'))
