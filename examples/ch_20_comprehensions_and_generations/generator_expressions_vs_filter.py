# usage: python3 generator_expressions_vs_filter.py

if __name__ == '__main__':
    print('code snippets from page 624\n')

    line = 'aa bbb c'

    # generator expression with if test
    print(''.join(x for x in line.split() if len(x) > 1))  # aabbb

    # NOTE: filter() produces a temporary list that the generator does not
    print(''.join(filter(lambda x: len(x) > 1, line.split())))  # aabbb
    print('')

    print(''.join(x.upper() for x in line.split() if len(x) > 1))  # AABBB

    # NOTE: adding processing steps to filter() requires a map(), which
    # increases complexity
    print(''.join(map(str.upper, filter(lambda x: len(x) > 1, line.split()))))

    # same as ^^^ using a loop
    res = ''
    for x in line.split():
        if len(x) > 1:
            res += x.upper()
    print(res)
