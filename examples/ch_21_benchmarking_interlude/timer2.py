'''
total(spam, 1, 2, a=3, b=4, _reps=1000) calls times spam(1, 2, a=3, b=4)
_reps times, and returns the total time for all runs with final result

bestof(spam, 1, 2, a=3, b=4, _reps=5) runs best-of-N timer to attempt to filter
out system load variation, and returns the best time among _reps tests

bestoftotal(spam, 1, 2, a=3, b=4, _reps1=5, reps=1000) runs best-of-totals
test, which takes the best among _reps1 runs of the total of _reps runs
'''

import time
# import sys

# NOTE: time.clock removed in python3 3.8
# timer = time.clock if sys.platform[:3] == 'win' else time.time
timer = time.time


# function calls the function passed to func using the positional arguments
# passed to pargs and the keyword args passed to kargs and retunrs a tuple
# that contains the total time elasped calling func as well as the result of
# the last call returned from func
# by default, this function will call func 1000 times, but if the caller
# specifies the _reps keyword argument, then func will be called _reps number
# of times
def total(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 1000)  # passed-in or default reps
    repslist = list(range(_reps))
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)


# function calls the function passed to func using the positional arguments
# passed to pargs and the keyword args passed to kargs and returns a tuple
# that contains the fastest time it took func() to return as well as the
# result of that call
# by default, this function will call func 5 times, but if the caller specifies
# the _reps keyword argument, then func will be called _reps number of times
def bestof(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 5)
    best = 2 ** 32
    for i in range(_reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best:
            best = elapsed
    return (best, ret)


# function returns a tuple that contains the fastest total time it takes to
# call the function passed to func with the positional arguments passed to
# pargs and keyword arguments passed to kargs as well as the results of that
# call
# by default, func will bell called 5 times, but if the caller specifies the
# _reps1 keyword argument, then func will be called _reps1 number of times
def bestoftotal(func, *pargs, **kargs):
    _reps1 = kargs.pop('_reps1', 5)
    return min(total(func, *pargs, **kargs) for i in range(_reps1))
