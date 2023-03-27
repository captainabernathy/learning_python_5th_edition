'''
Same usage as timer2.py, but uses 3.X keyword-only default arguments instead of
dict pops for simpler code. No need to hoist range() out of test in 3.X: always
a generator in 3.X... cannot run on 2.X
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
def total(func, *pargs, _reps=1000, **kargs):
    start = timer()
    for i in range(_reps):
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)


# function calls the function passed to func using the positional arguments
# passed to pargs and the keyword args passed to kargs and returns a tuple
# that contains the fastest time it took func() to return as well as the
# result of that call
# by default, this function will call func 5 times, but if the caller specifies
# the _reps keyword argument, then func will be called _reps number of times
def bestof(func, *pargs, _reps=5, **kargs):
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
def bestoftotal(func, *pargs, _reps1=5, **kargs):
    return min(total(func, *pargs, **kargs) for i in range(_reps1))
