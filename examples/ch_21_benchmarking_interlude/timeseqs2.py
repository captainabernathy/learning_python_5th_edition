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
def forLoop():
    res = []
    for x in repslist:
        res.append(x + 10)
    return res


# function returns a list comprehension that computes the sum of 10 and every
# number between 0 and 9999
def listComp():
    return [x + 10 for x in repslist]


# function returns a list that maps a lambda function that returns the sum
# of 10 and its argument to every number between 0 and 9999
def mapCall():
    return list(map((lambda x: x + 10), repslist))


# function that returns a list that uses a generator expression to compute
# the sum of 10 and every number between 0 and 9999
def genExpr():
    return list(x + 10 for x in repslist)


# function that returns a list that calls a generator function to yield the
# sum of 10 and every number between 0 and 9999
def genFunc():
    def gen():
        for x in repslist:
            yield x + 10
    return list(gen())


if __name__ == '__main__':
    print('code snippets from pages 659-660\n')

    print(sys.version)
    for test in (forLoop, listComp, mapCall, genExpr, genFunc):
        (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
        print('%-9s: %.5f => [%s...%s]' %
              (test.__name__, bestof, result[0], result[-1]))
