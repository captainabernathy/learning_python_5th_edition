# usage: python3 list_comprehensions_vs_map.py

if __name__ == '__main__':
    print('code snippets from pages 604-605\n')

    res = []
    for x in 'spam':
        res.append(ord('x'))

    print(res)  # ['s','p','a','m']

    # NOTE: map() maps a fuction over an iterable, so it's necessary to
    # construct its result into the appropriate type
    res = list(map(ord, 'spam'))
    print(res)  # ['s','p','a','m']

    # NOTE: list comprehensions map an expression over an iterable
    res = [ord(x) for x in 'spam']
    print(res)  # ['s','p','a','m']
    print('')

    print([x ** 2 for x in range(10)])  # [0,1,4,9,25,36,49,64,81]
    print(list(map(lambda x: x ** 2, range(10))))  # same as ^^^ map and lambda
