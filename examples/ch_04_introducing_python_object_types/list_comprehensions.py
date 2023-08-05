# usage: python3 list_comprehensions.py

if __name__ == '__main__':
    print('code snippets from pages 114-116\n')

    M = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    print(M)

    # grab a column with a list comprehension
    col2 = [row[1] for row in M]
    print(col2)  # [2,5,8]

    # add 1 to each item in column 2
    print([row[1] + 1 for row in M])  # [3,6,9]

    # filter out odd items in column 2
    print([row[1] for row in M if row[1] % 2 == 0])  # [2,8]

    # get matrix diagonal
    diag = [M[i][i] for i in [0, 1, 2]]
    print(diag)  # [1,5,9]

    # repeat characters in a string
    doubles = [c * 2 for c in 'spam']
    print(doubles)  # ['ss', 'pp', 'aa', 'mm']

    # generate a successive range of integers
    print(list(range(4)))  # [0,1,2,3]

    # generate range from -6 to +6 by 2
    print(list(range(-6, 7, 2)))  # [-6,-4,...,4,6]

    # generate squares and cubes for a range
    # [[0,0], [1,1], [4,8], [9,27]]
    print([[x ** 2, x ** 3] for x in range(4)])

    # more compilcated example
    print([[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0])

    # generators...
    # use sum() to calculate items in a sequence...

    # Create a generator of row sums
    G = (sum(row) for row in M)
    print(next(G))  # 6
    print(next(G))  # 15
    print(next(G))  # 24

    # alternatively use map()
    print(list(map(sum, M)))  # [6,15,24]

    # create a set of row sums
    print({sum(row) for row in M})  # {24,6,15}

    # create a dictionary of row:sum pairs
    # set comprehension
    print({i: sum(M[i]) for i in range(3)})  # {0:6,1:15,2:24}

    # list of character ordinals
    print([ord(x) for x in 'spaam'])  # [115,112,97,97,109]

    # set of character ordinals
    print({ord(x) for x in 'spaam'})  # {112,97,115,109}

    # dictionary comprehension
    # dictionary of character:ordinal pairs
    # {'s':115, 'p':112, 'a':97, 'm':109}
    print({x: ord(x) for x in 'spaam'})

    # generator of ordinals
    g = (ord(x) for x in 'spaam')
    print(next(g))  # 115
    print(next(g))  # 97
    print(next(g))  # 97
    print(next(g))  # 97
    print(next(g))  # 109
