# usage: python3 new_iterables_in_python_3x.py

if __name__ == '__main__':
    print('code snippets from pages 451-452\n')

    # for each integer between zero and three (exclusive), raise 2 to the power
    # of that integer
    M = map(lambda x: 2 ** x, range(3))

    # NOTE: a map object only supports a single iteration
    # additionally map and zip object are NOT subscriptable
    for i in M:
        print(i)  # 1,2,4

    for i in M:  # nothing... M is exhausted in a single pass
        print(i)  # loop body is never executed
