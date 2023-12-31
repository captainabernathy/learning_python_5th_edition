# usage: python3 timeseqs_timer2.py

'''Test the relative speed of iteration tool alternatives: timer2 version'''
import sys
import timer2
reps = 10000
repslist = list(range(reps))


# function returns a list that contains the absolute value of of the numbers
# from 0 to 9999
def for_loop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res


# function returns a list comprehension that computes the absolute value of
# every number between 0 and 9999
def list_comp():
    return [abs(x) for x in repslist]


# function returns a list that maps a lambda function that returns the absolute
# value of its argument for every number between 0 and 9999
def map_call():
    return list(map(abs, repslist))


# function that returns a list that uses a generator expression to compute
# the absolute value of every number between 0 and 9999
def gen_expr():
    return list(abs(x) for x in repslist)


# function that returns a list that contains the result of using a generator
# function to yield the absolute value of the numbers from 0 to 9999
def gen_func():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())


# function returns the result of the sum of its arguments
def spam(a, b, c, d):
    return a + b + c + d


if __name__ == '__main__':
    print('code snippets from pages 661-663\n')

    print(sys.version)
    for test in (for_loop, list_comp, map_call, gen_expr, gen_func):
        (total, result) = timer2.bestoftotal(test, _reps1=5, _reps=1000)

        print('%-9s: %.5f => [%s...%s]' %
              (test.__name__, total, result[0], result[-1]))
    print('')

    print(timer2.total(spam, 1, 2, c=3, d=4, _reps=1000))
    print('')
    
    print(timer2.bestof(spam, 1, 2, c=3, d=4, _reps=1000))
    print('')

    print(timer2.bestoftotal(spam, 1, 2, c=3, d=4, _reps1=1000, _reps=1000))
    print('')

    print(timer2.bestoftotal(spam, *(1, 2), _reps1=1000, _reps=1000,
          **dict(c=3, d=4)))
