# usage: python3 timing_iterations_with_timeit.py

import timeit

# NOTE: with the timeit module, tests are specified by either callable objects
# or statement strings


# function that returns a list comprehension that computes the square of each
# of the numbers from 0 to 999
def testcase():
    [x ** 2 for x in range(1000)]  # callable objects or string code


if __name__ == '__main__':
    print('code snippets from pages 666-669\n')

    # NOTE: the timeit module's repeat() function returns a list that gives
    # the total time taken to run a test a given number of times
    # for each of the repeat runs, the min of the list yields the best time
    # among the runs, and helps filter out system load fluctuations that can
    # otherwise skew timing results
    print(min(timeit.repeat(stmt="[x ** 2 for x in range(1000)]", number=1000,
          repeat=5)))

    # timing multiline statements
    print(min(timeit.repeat(number=1000, repeat=3,
          stmt="L = [1, 2, 3, 4]\nfor i in range(len(L)): L[i] += 1")))

    print(min(timeit.repeat(number=10000, repeat=3,
          stmt="L = [1, 2, 3, 4, 5]\ni = 0\nwhile i < len(L):\n\ti += 1")))

    print(min(timeit.repeat(number=10000, repeat=3,
          stmt="L = [1, 2, 3, 4, 5]\nM = [x + 1 for x in L]")))
    print('')

    # other usage modes: setup, totals, and objects
    # NOTE: setup code is run in the main statement's scope but not charged to
    # the main statement's total (initialization code)
    print(min(timeit.repeat(number=1000, repeat=3,
          setup='from mins import min1, min2, min3\n'
          'vals=list(range(1000))', stmt='min3(*vals)')))
    print('')

    # total time... via timeit.timeit()
    print(timeit.timeit(stmt='[x ** 2 for x in range(1000)]', number=1000))

    # class api calls... timeit.Timer(c_args).method(m_args)
    print(timeit.Timer(stmt='[x ** 2 for x in range(1000)]').timeit(1000))

    # api call... timeit.repeat()
    print(timeit.repeat(stmt='[x ** 2 for x in range(1000)]', number=1000,
          repeat=3))
    print('')

    print(min(timeit.repeat(stmt=testcase, number=1000, repeat=3)))
