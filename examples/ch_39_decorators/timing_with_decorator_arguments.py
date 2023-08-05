# usage: python3 timing_with_decorator_arguments.py

from timerdeco2 import timer


@timer(trace=False)
def listcomp1(N):  # listcomp1 = timer(False)(listcomp1)
    return [x * 2 for x in range(N)]


@timer(trace=True, label='\t=>')
def listcomp2(N):  # listcomp2 = timer(True,'\t=>')(listcomp2)
    return [x * 2 for x in range(N)]


# for illustrative purposes
def listcomp11(N):
    return [x * 2 for x in range(N)]


def listcomp22(N):
    return [x * 2 for x in range(N)]


if __name__ == '__main__':
    print('code snippets from page 1346\n')

    x = listcomp1(5000)
    x = listcomp1(5000)
    x = listcomp1(5000)

    print(listcomp1.alltime)
    print('')

    x = listcomp2(5000)
    x = listcomp2(5000)
    x = listcomp2(5000)
    print('')

    print(listcomp2.alltime)
    print('')

    print('-' * 80)
    print('')

    # for illustrative purposes....
    t11 = timer(trace=False)(listcomp11)
    x = t11(5000)
    x = t11(5000)
    x = t11(5000)

    print(t11.alltime)
    print('')

    t22 = timer('\t=>', True)(listcomp22)
    x = t22(5000)
    x = t22(5000)
    x = t22(5000)
    print('')

    print(t22.alltime)
    print('')
