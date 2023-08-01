import sys
from timerdeco2 import timer

force = list if sys.version_info[0] == 3 else (lambda X: X)


@timer(label='[CCC]==>')
def listcomp(N):  # listcomp = timer(label='[CCC]==>')listcomp)
    return [x * 2 for x in range(N)]  # listcomp(...) triggers Timer.__call__


@timer(trace=True, label='[MMM]==>')
def mapcall(N):  # mapcall = timer(trace=True, label='[MMM]==>')(mapcall)
    return force(map((lambda x: x * 2), range(N)))


# for illustrative purposes...
def lcomp(N):
    return [x * 2 for x in range(N)]


def mapc(N):
    return force(map((lambda x: x * 2), range(N)))


if __name__ == '__main__':
    print('code snippets from page 1345\n')

    for func in (listcomp, mapcall):
        result = func(5)  # time for this call, all calls, return value
        print('')
        func(50000)
        print('')
        func(500000)
        print('')
        func(1000000)
        print('')
        print(result)
        print('')
        print('alltime = %s\n' % func.alltime)  # total time for all calls
        print('')

    print('**map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))

    print('')
    print('-' * 80)
    print('')

    # for illustrative purposes...
    tlc = timer('[CCC]==>')(lcomp)
    tmc = timer('[MMM]==>')(mapc)
    for func in (tlc, tmc):
        result = func(5)  # time for this call, all calls, return value
        print('')
        func(50000)
        print('')
        func(500000)
        print('')
        func(1000000)
        print('')
        print(result)
        print('')
        print('alltime = %s\n' % func.alltime)  # total time for all calls
        print('')

    print('**map/comp = %s' % round(tmc.alltime / tlc.alltime, 3))
    print('')
