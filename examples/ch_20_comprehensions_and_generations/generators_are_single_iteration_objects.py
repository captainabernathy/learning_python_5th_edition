# usage: python3 generators_are_single_iteration_objects.py

# generator function that for each element in S, yields the result of that
# element times for for any element that defines multiplication
def timesfour(S):
    for c in S:
        yield c * 4


if __name__ == '__main__':
    print('code snippets from pages 627-628\n')

    # generator expression equivalent to timesfour()
    G = (c * 4 for c in 'SPAM')
    
    # NOTE: generator expressions and functions only support single iterators
    print(iter(G) is G)  # True
    print('')

    I1 = iter(G)
    print(next(I1))  # SSSS
    print(next(I1))  # PPPP
    print('')

    I2 = iter(G)
    print(I2 is G)  # True
    print(I1 is I2)  # True
    print('')
    
    print(next(I2))  # AAAA
    print(list(I1))  # ['MMMM']
    print('')

    # I3 = iter(G)  # is at end...
    I3 = iter(c * 4 for c in 'SPAM')  # need new generator to start over
    print(next(I3))  # SSSS
    print('')

    G = timesfour('spam')
    print(iter(G) is G)  # True
    print('')

    I1, I2 = iter(G), iter(G)
    I3 = I2
    print(next(I1))  # ssss
    print(next(I2))  # pppp
    print(next(I3))  # aaaa
    print(next(G))  # mmmm
