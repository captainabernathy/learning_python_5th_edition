# usage: python3 timeseqs2B.py

'''
See effect of function call in all
'''
import sys
import timer
reps = 10000
repslist = list(range(reps))


# function that returns the argument it was passed
def F(x):
    return x


# function returns a list that contains the result of calling the function F()
# on every number between 0 and 9999
def for_loop():
    res = []
    for x in repslist:
        res.append(F(x))
    return res


# function that returns a list comprehension that contains the result of
# calling the function F() on every number between 0 and 9999
def list_comp():
    return [F(x) for x in repslist]


# function that returns a list that contains the result of mapping the function
# F() on every number between 0 and 9999
def map_call():
    return list(map(F, repslist))


# function that returns a list that contains the result of using a generator
# expression to call the function F() on every number between 0 and 9999
def gen_expr():
    return list(F(x) for x in repslist)


# function that returns a list that calls a generator function to yield the
# result of calling the function F() on every number between 0 and 9999
def gen_func():
    def gen():
        for x in repslist:
            yield F(x)
    return list(gen())


if __name__ == '__main__':
    print('code snippets from page 661\n')

    print(sys.version)
    for test in (for_loop, list_comp, map_call, gen_expr, gen_func):
        (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
        print('%-9s: %.5f => [%s...%s]' %
              (test.__name__, bestof, result[0], result[-1]))
