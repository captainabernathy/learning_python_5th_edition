import timer

if __name__ == '__main__':
    print('code snippets from pages 653-655\n')
    # total time it takes to run pow(2,1000) 1000 times
    print(timer.total(1000, pow, 2, 1000)[0])
    print('')
    
    # total time it takes to run str.upper('spam') 1000 times and the last
    # result ('SPAM')
    print(timer.total(1000, str.upper, 'spam'))
    print('')

    # fastest time of 1000 calls to call pow(2,1000000)
    print(timer.bestof(1000, pow, 2, 1000000)[0])
    print('')

    # fastest time of 50 calls to the result of the total time it takes to
    # call str.upper('spam') 1000 times accompanied by that result
    print(timer.bestof(50, timer.total, 1000, str.upper, 'spam'))
    print('')

    # same as ^^^ using best of total
    print(timer.bestoftotal(50, 1000, str.upper, 'spam'))
    print('')

    # the fastest of 50 iterations of the time it takes to call
    # str.upper('spam') 1000 times... similar to the second element of the
    # tuple returned from bestoftotal()
    print(min(timer.total(1000, str.upper, 'spam') for i in range(50)))
