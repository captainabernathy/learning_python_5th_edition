# usage: python3 timeseqs.py

''' Module tests the relative speed of iteration tool alternatives '''
import sys
import timer

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
# the numbers from 0 to 9999
def list_comp():
    return [abs(x) for x in repslist]


# function returns a list that maps the absolute function to the numbers from
# 0 to 9999
def map_call():
    return list(map(abs, repslist))


# function returns a list that uses a generator expression to compute the
# absolute value of the numbers of 0 to 9999
def gen_expr():
    return list(abs(x) for x in repslist)


# function that returns a list that contains the result of using a generator
# function to yield the absolute value of the numbers 0 to 9999
def gen_func():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())  # list() forces results


if __name__ == '__main__':
    print('code snippets from pages 656-657\n')

    print(sys.version)
    for test in (for_loop, list_comp, map_call, gen_expr, gen_func):
        (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
        print('%-9s: %.5f => [%s...%s]' %
              (test.__name__, bestof, result[0], result[-1]))
