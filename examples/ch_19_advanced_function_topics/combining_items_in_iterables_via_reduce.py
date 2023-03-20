from functools import reduce
import operator


# function accumulates the result of successively applying func to the elements
# in seq and returns the result
def myreduce(func, seq):
    tot = seq[0]
    for next in seq[1:]:
        tot = func(tot, next)
    return tot


if __name__ == '__main__':
    print('code snippets from pages 599-600\n')
    print(reduce((lambda x, y: x + y), [1, 2, 3, 4]))  # 10
    print('')

    print(reduce((lambda x, y: x * y), [1, 2, 3, 4]))  # 24
    print('')

    # similarly... accumulate the result of successively applying an
    # operation to each element in a sequenece in a loop
    L = [1, 2, 3, 4]
    res = L[0]
    for x in L[1:]:
        res += x

    print(res)  # 10
    print('')

    print(myreduce((lambda x, y: x + y), [1, 2, 3, 4, 5]))  # 15
    print('')

    print(myreduce((lambda x, y: x * y), [1, 2, 3, 4, 5]))  # 120
    print('')

    print(reduce(operator.add, [2, 3, 4]))  # 9
    print('')

    print(reduce((lambda x, y: x + y), [2, 4, 6]))  # 12
