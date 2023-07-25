if __name__ == '__main__':
    print('code snippets from pages 647-648\n')
    print({x * x for x in range(10)})  # {0,1,64,4,36,9,16,49,81,25}
    print(set(x * x for x in range(10)))  # {0,1,64,4,36,9,16,49,81,25}
    print('')

    # {0:0,1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81}
    print({x: x * x for x in range(10)})

    # {0:0,1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81}
    print(dict((x, x * x) for x in range(10)))
    print('')

    # set comprehension equivalent
    res = set()
    for x in range(10):
        res.add(x * x)
    print(res)  # {0,1,64,4,36,9,16,49,81,25}
    print('')

    # dictionary comprehension equivalent
    res = {}
    for x in range(10):
        res[x] = x * x
    print(res)  # {0:0,1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81}
    print('')

    # generator expression
    G = ((x, x * x) for x in range(10))

    try:
        while True:
            # (0,0), (1,1), (2,4), (3,9), (4,16), (5,25), (6,36), (7,49),
            # (8,64), (9,81)
            print(next(G))
    except StopIteration:
        pass
