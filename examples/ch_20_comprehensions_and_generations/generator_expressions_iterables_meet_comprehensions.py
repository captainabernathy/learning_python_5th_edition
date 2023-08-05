# usage: python3 generator_expressions_iterables_meet_comprehensions.py

if __name__ == '__main__':
    print('code snippets from pages 620-621\n')

    print([x ** 2 for x in range(4)])  # list comprehension... build a list
    print(list(x ** 2 for x in range(4)))  # [0,1,4,9] same as ^^^
    print('')

    G = (x ** 2 for x in range(4))  # generator expressions... make an iterable

    try:
        while True:
            print(next(G))  # 0 1 4 9
    except StopIteration:
        pass
    print('')
    
    for num in (x ** 2 for x in range(4)):  # calls next() automatically
        print('%s, %s' % (num, num / 2.0))  # 0 0.0, 1 0.5, 4 2.0, 9 4.5
    print('')

    # NOTE: here join() runs the generator expression
    # AAABBBCCC
    print(''.join(x.upper() for x in 'aaa,bbb,ccc'.split(',')))
    print('')

    a, b, c = (x + '\n' for x in 'aaa,bbb,ccc'.split(','))
    print(a)  # aaa
    print(b)  # bbb
    print(c)  # ccc
    print('')

    # NOTE: parentheses are not required around a generator expression that
    # is the sole item item already enclosed in parentheses used for other
    # purposes
    print(sum(x ** 2 for x in range(4)))  # no extra parentheses required
    print(sorted(x ** 2 for x in range(4)))  # no extra parentheses required

    # parentheses are required here bc the generator expression is not the
    # only item in the call to sorted()
    print(sorted((x ** 2 for x in range(4)), reverse=True))
