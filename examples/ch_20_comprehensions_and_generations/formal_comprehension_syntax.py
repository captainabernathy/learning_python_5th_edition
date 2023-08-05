# usage: python3 formal_comprehension_syntax.py

if __name__ == '__main__':
    print('code snippets from page 607\n')

    # list comprehension that adds the each element in the first list to
    # each element in the second list
    res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
    print(res)  # [100,200,300,101,201,301,102,202,302]

    # same as ^^^ with loops
    # append the result of adding each element in the first list to each
    # element in the second list
    res = []
    for x in [0, 1, 2]:
        for y in [100, 200, 300]:
            res.append(x + y)

    print(res)  # [100,200,300,101,201,301,102,202,302]
    print('')

    # list comprehension that concatenates each letter in the first string
    # to each letter in the second string
    # ['sS','sP','sA','sM',...,'mS','mP','mA','mM']
    print([x + y for x in 'spam' for y in 'SPAM'])

    # same as ^^^ using loops
    res = []
    for x in 'spam':
        for y in 'SPAM':
            res.append(x + y)

    print(res)
    print('')

    # ['sP','sA', 'mP','mA']
    print([x + y for x in 'spam'
           if x in 'sm' for y in 'SPAM' if y in ('P', 'A')])

    # same as ^^^ using loops
    res = []
    for x in 'spam':
        if x in 'sm':
            for y in 'SPAM':
                if y in ('P', 'A'):
                    res.append(x + y)
    print(res)
    print('')

    # ['sP2','sP3','sA2','sA3','mP2','mP3','mA2','mA3']
    print([x + y + z for x in 'spam' if x in 'sm'
          for y in 'SPAM' if y in ('P', 'A') for z in '123' if z > '1'])

    # same as ^^^ using loops
    res = []
    for x in 'spam':
        if x in 'sm':
            for y in 'SPAM':
                if y in ('P', 'A'):
                    for z in '123':
                        if z > '1':
                            res.append(x + y + z)

    print(res)
    print('')

    # [(0,1),(0,3),(2,1),(2,3),(4,1),(4,3)]
    print([(x, y) for x in range(5) if not x % 2 for y in range(5) if y % 2])

    # same as ^^^ using loops
    res = []
    for x in range(5):
        if not x % 2:
            for y in range(5):
                if y % 2:
                    res.append((x, y))

    print(res)
