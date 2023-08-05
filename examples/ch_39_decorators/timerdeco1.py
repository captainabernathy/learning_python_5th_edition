# usage: python3 timerdeco1.py

# program times calls made to a decorated function -- bot the time for one
# call, and the total time among calls
#
# the decorator is applied to two function in order to compare the relative
# speed of list comprehensions and the map built-in
import sys
import time

force = list if sys.version_info[0] == 3 else (lambda X: X)


class timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        elapsed = time.time() - start
        self.alltime += elapsed
        print('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
        return result


@timer
def listcomp(N):
    return [x * 2 for x in range(N)]


@timer
def mapcall(N):
    return force(map((lambda x: x * 2), range(N)))


# for illustrative purposes...
def lcomp(N):
    return [x * 2 for x in range(N)]


def mapc(N):
    return force(map((lambda x: x * 2), range(N)))


if __name__ == '__main__':
    print('code snippets from pages 1340-1341\n')

    result = listcomp(5)  # time for this call, all calls, return value
    print('')

    listcomp(50000)
    print('')

    listcomp(500000)
    print('')

    listcomp(1000000)
    print('')

    print(result)
    print('')

    print('alltime = %s' % listcomp.alltime)  # total time for listcomp calls
    print('')

    result = mapcall(5)
    print('')

    mapcall(50000)
    print('')

    mapcall(500000)
    print('')

    mapcall(1000000)
    print('')

    print(result)
    print('')

    print('alltime = %s' % mapcall.alltime)  # total time for mapcall calls
    print('')

    print('\n**map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))
    print('')

    print('-' * 80)
    print('')

    # for illustrative purposes
    tlc = timer(lcomp)
    result = tlc(5)
    print('')
    tlc(50000)
    print('')
    tlc(500000)
    print('')
    tlc(1000000)
    print('')
    print(result)
    print('')
    print('alltime = %s' % tlc.alltime)
    print('')

    tmc = timer(mapc)
    result = tmc(5)
    print('')
    tmc(50000)
    print('')
    tmc(500000)
    print('')
    tmc(1000000)
    print('')
    print(result)
    print('')
    print('alltime = %s' % tmc.alltime)
    print('')
    print('\n**map/comp = %s' % round(tmc.alltime / tlc.alltime, 3))
    print('')
