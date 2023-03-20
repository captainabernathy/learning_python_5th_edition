import sys

if __name__ == '__main__':
    print('code snippets from page 594\n')
    # NOTE: the body of a lambda function must be a single expression... NOT a
    # series of statements
    lower = (lambda x, y: x if x < y else y)
    print(lower('bb', 'aa'))  # aa
    print(lower('aa', 'bb'))  # aa
    print('')

    # NOTE: to perform a loop-like action in a lambda, use map() calls or
    # comprehensions
    showall = (lambda x: list(map(sys.stdout.write, x)))  # 3.X must use list
    t = showall(['spam\n', 'toast\n', 'eggs\n'])  # outputs arguments
    print(t)  # [5 6 5]... number of bytes written by write()
    print('')

    # same as map() call above but with list comprehension
    showall = (lambda x: [sys.stdout.write(line) for line in x])
    t = showall(['bright\n', 'side\n', 'of\n', 'life\n'])
    print(t)  # [7,5,3,5]... number of bytes written by write()
    print('')

    # similar to ^^^, but with print() instead of write
    showall = (lambda x: [print(line, end='') for line in x])  # 3.X only
    t = showall(['spam\n', 'toast\n', 'eggs\n'])  # outputs arguments
    print(t)  # [None, None, None]... print returns None!
    print('')

    # similar to ^^^, but with * argument instead of list comprehension
    showall = (lambda x: print(*x, sep='', end=''))
    t = showall(['bright\n', 'side\n', 'of\n', 'life\n'])
    print(t)  # [None]... * argument counts as a single argument

