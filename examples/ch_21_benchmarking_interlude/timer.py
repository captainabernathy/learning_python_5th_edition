'''
Homegrown timing tools for function calls.
Does total time, best-of time, and best-of-totals time
'''

import time
# import sys

# NOTE: time.clock removed in python3 3.8
# timer = time.clock if sys.platform[:3] == 'win' else time.time
timer = time.time

# NOTE: this module improves on the module timer0 in the following ways:
# a. the range() call is hoisted out of the timing loop in total()
# b. the reps count is passed in as an argument
# c. any number of positional arguments are collected in *pargs, and any number
#    of keyword arguments are collected in **kargs


# function calls the function passed to func using the positional arguments
# passed to pargs and the keyword args passed to kargs a total of reps times
# and returns the total time elasped and the result of the last call in a tuple
def total(reps, func, *pargs, **kargs):
    '''
    Total time to run func() reps times
    Returns (total time, last result)
    '''
    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)


# function calls the function passed to func using the positional arguments
# passed to pargs and the keyword args passed to kargs a total of reps times
# and returns the best time and result in a tuple
def bestof(reps, func, *pargs, **kargs):
    '''
    Quickest func() among reps runs
    Returns (best time, last result)
    '''
    best = 2 ** 32
    for i in range(reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best:
            best = elapsed
    return (best, ret)


# function returns a tuple that contains the lowest time of reps1 runs of reps2
# calls to func using the positional arguments passed to pargs and the keyword
# arguments passed to kargs
def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    '''
    Best of totals
    (best of reps1 runs of (total reps2 runs of func))
    '''
    return bestof(reps1, total, reps2, func, *pargs, **kargs)
