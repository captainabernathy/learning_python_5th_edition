# usage: python3 timeseqs2.py

'''
See effect of function call in map only
'''
import sys
import timer
reps = 10000
repslist = list(range(reps))


# function returns a list that contains the sum of 10 and every number between
# 0 and 9999
def for_loop():
    res = []
    for x in repslist:
        res.append(x + 10)
    return res


# function returns a list comprehension that computes the sum of 10 and every
# number between 0 and 9999
def list_comp():
    return [x + 10 for x in repslist]


# function returns a list that maps a lambda function that returns the sum
# of 10 and its argument to every number between 0 and 9999
def map_call():
    return list(map((lambda x: x + 10), repslist))


# function that returns a list that uses a generator expression to compute
# the sum of 10 and every number between 0 and 9999
def gen_expr():
    return list(x + 10 for x in repslist)


# function that returns a list that calls a generator function to yield the
# sum of 10 and every number between 0 and 9999
def gen_func():
    def gen():
        for x in repslist:
            yield x + 10
    return list(gen())


if __name__ == '__main__':
    print('code snippets from pages 659-660\n')

    print(sys.version)
    for test in (for_loop, list_comp, map_call, gen_expr, gen_func):
        (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
        print('%-9s: %.5f => [%s...%s]' %
              (test.__name__, bestof, result[0], result[-1]))
