# usage: python3 generator_expressions_vs_map.py

import math

if __name__ == '__main__':
    print('code snippets from pages 622-623\n')

    # map a function on a tuple
    print(list(map(abs, (-1, -2, 3, 4))))  # [-1,-2,3,4]

    # apply function to results yielded from generator expression
    print(list(abs(x) for x in (-1, -2, 3, 4)))  # [-1,-2,3,4]
    
    # map a lambda "function" on a tuple
    print(list(map(lambda x: x * 2, (1, 2, 3, 4))))  # nonfunction case

    # same as ^^^ using a generator expression... no need to use map() or
    # lambda
    print(list(x * 2 for x in (1, 2, 3, 4)))  # [2,4,6,8]... generator
    print('')

    line = 'aaa,bbb,ccc'
    
    # makes a pointless list
    print(''.join([x.upper() for x in line.split(',')]))  # AAABBBCCC
    
    # no need to wrap the argument to join() in a list since it automatically
    # processes generator expressions
    print(''.join(x.upper() for x in line.split(',')))  # generates results

    # iterables returned by map() in 3x are similar to those returned from
    # generator expressions bc they both generate results on request
    print(''.join(map(str.upper, line.split(','))))  # generates results
    
    print(''.join(x * 2 for x in line.split(',')))  # generator

    # calls to map the require a lambda function are often more cumbersome than
    # accomplishing the same results with a generator expression
    print(''.join(map(lambda x: x * 2, line.split(','))))
    print('')

    # nested list comprehensions
    print([x * 2 for x in [abs(x) for x in (-1, -2, 3, 4)]])  # [2,4,6,8]
    
    # nested maps
    print(list(map(lambda x: x * 2, map(abs, (-1, -2, 3, 4)))))  # [2,4,6,8]

    # nested generator expressions
    print(list(x * 2 for x in (abs(x) for x in (-1, -2, 3, 4))))  # [2,4,6,8]
    print('')

    # map on a nested generator expression
    print(list(map(math.sqrt, (x ** 2 for x in range(4)))))  # [0,1,2,3]
    print('')

    print(list(map(abs, map(abs, map(abs, (-1, 0, 1))))))  # nesting gone bad
    print('')

    # unnested generator expressions that produce the same results as ^^^
    print(list(abs(x) * 2 for x in (-1, -2, 3, 4)))  # [2,4,6,8]
    print(list(math.sqrt(x ** 2) for x in range(4)))  # [0,1,2,3]
    print(list(map(abs, (-1, 0, 1))))
