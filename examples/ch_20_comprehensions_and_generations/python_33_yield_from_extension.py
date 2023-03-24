# generator function that yields results, firstly for each integer in the range
# [0,N-1], and secondarily for the square of each integer in the range in
# [0,N-1]
def both1(N):
    for i in range(N):
        yield i
    for i in (x**2 for x in range(N)):
        yield i


# NOTE: python 3.3 extended the syntax for the yield statement, which allows it
# to delegate to a subgenerator with a from clause
# generator function that yields results, firstly for each integer in the range
# [0,N-1], and secondarily for the square of each integer in the range in
# [0,N-1]
def both2(N):
    yield from range(N)
    yield from (x ** 2 for x in range(N))


if __name__ == '__main__':
    print('code snippets from pages 628-629\n')
    # in these examples, the list() constructor forces the generators produce
    # all of their results
    print(list(both1(5)))  # [0,1,2,3,4,0,1,4,9,16]
    print('')

    print(list(both2(5)))  # [0,1,2,3,4,0,1,4,9,16]
    print('')

    # 0 : 1 : 2 : 3 : 4 : 0 : 1 : 4 : 9 : 16
    print(' : '.join(str(i) for i in both2(5)))
