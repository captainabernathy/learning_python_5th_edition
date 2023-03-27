from timer0 import timer

if __name__ == '__main__':
    # program tests the timer() function from the timer0 module
    print('code snippets from page 652\n')
    print(timer(pow, 2, 1000))
    print(timer(str.upper, 'spam'))
