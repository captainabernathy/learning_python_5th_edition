# usage: python3 generator_functions_vs_generator_expressions.py

# generator function that for each element in S, yields the result of that
# element times for for any element that defines multiplication
def timesfour(S):  # generator function
    for c in S:
        yield c * 4


# generator function that takes a space delimitted line, splits it and yields
# the result of capitalizing each of the parts that are more than one letter
def gensub(line):
    for x in line.split():
        if len(x) > 1:
            yield x.upper()


if __name__ == '__main__':
    print('code snippets from pages 625-626\n')

    G = (c * 4 for c in 'SPAM')  # generator expression... same as timesfour()
    print(list(G))  # ['SSSS','PPPP','AAAA','MMMM']... evaulation

    G = timesfour('spam')
    print(list(G))  # ['ssss','pppp','aaaa','mmmm']
    print('')

    G = (c * 4 for c in 'SPAM')
    # NOTE: the iter() function returns an iterator to an iterable object
    It = iter(G)
    # manually iterate over the result of a generator expression
    try:
        while True:
            print(next(It))  # SSSS PPPP AAAA MMMM
    except StopIteration:
        pass
    print('')

    G = timesfour('spam')
    It = iter(G)
    # manually iterate over the result of a generator function
    try:
        while True:
            print(next(It))  # ssss pppp aaaa mmmm
    except StopIteration:
        pass
    print('')

    line = 'aa bbb c'
    # generator expression equivalent to generator function gensub()
    # AABBB
    print(''.join(x.upper() for x in line.split() if len(x) > 1))

    # AABBB
    print(''.join(gensub(line)))
