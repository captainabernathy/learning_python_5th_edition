import time


# function returns the total time taken to run 1000 calls to the function
# passed to func with arbitrary positional arguments
# NOTE: The Limitations of this function
# a. Doesn't support keyword arguments in the tested function call
# b. Hardcodes the repetitions count
# c. Charges the cost of range() to the tested function's time
# d. Doesn't give callers a way to verify that the tested function actually
#    worked
# e. Only gives total time, which might fluctuate on heavily loaded machines
def timer(func, *args):  # simplistic timing function
    # start = time.clock()  # removed in python 3.8
    start = time.time()
    for i in range(1000):
        func(*args)  # call func with args
    # return time.clock() - start  # total elapsed time in seconds
    return time.time() - start
