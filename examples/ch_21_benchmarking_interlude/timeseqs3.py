'''
Very similar to pybench.py's timeit total, but still not identical: adds
function call per total loop, uses prebuilt list for range instead of generator
'''
import sys
import timer
reps = 1000
repslist = list(range(reps))


# function returns a list that contains the square of of the numbers from 0 to
# 9999
def forLoop():
    res = []
    for x in repslist:
        res.append(x ** 2)
    return res


# function returns a list comprehension that computes the square of every
# number from 0 to 9999
def listComp():
    return [x ** 2 for x in repslist]


# function returns a list that maps a lambda function that returns the square
# of its argument for every number between 0 and 9999
def mapCall():
    return list(map((lambda x: x ** 2), repslist))


# function that returns a list that uses a generator expression to compute
# the square of every number between 0 and 9999
def genExpr():
    return list(x ** 2 for x in repslist)


# function that returns a list that contains the result of using a generator
# function to yield the square of the numbers from 0 to 9999
def genFunc():
    def gen():
        for x in repslist:
            yield x ** 2
    return list(gen())


if __name__ == '__main__':
    print('code snippets from page 676\n')
    print(sys.version)
    for test in (forLoop, listComp, mapCall, genExpr, genFunc):
        (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
        print('%-9s: %.5f => [%s...%s]' %
              (test.__name__, bestof, result[0], result[-1]))
