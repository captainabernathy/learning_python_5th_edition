# usage: python3 list_comprehensions_and_matricies.py

if __name__ == '__main__':
    print('code snippets from pages 608-610\n')

    M = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    N = [[2, 2, 2],
         [3, 3, 3],
         [4, 4, 4]]

    print(M)  # [[1,2,3],[4,5,6],[7,8,9]]
    print('')
    print(N)  # [[2,2,2],[3,3,3],[4,4,4]]
    print('')

    print([row[1] for row in M])  # [2,5,8]... second column
    print('')

    print([M[row][1] for row in range(3)])  # [2,5,8]... same as ^^^
    print('')

    for row in M:
        print(row[1], end=' ')  # 2 5 8... same as ^^^
    print('\n')

    # diagonal left-to-right
    print([M[i][i] for i in range(len(M))])  # [1,5,9]
    print('')

    # diagonal right-to-left
    print([M[i][len(M) - 1 - i] for i in range(len(M))])  # [7,5,3]
    print('')

    L = [[1, 2, 3], [4, 5, 6]]
    print(L)  # [[1,2,3],[4,5,6]]
    print('')
    for i in range(len(L)):
        for j in range(len(L[i])):
            L[i][j] += 10
    print(L)  # [[11,12,13],[14,15,16]]
    print('')

    print([col + 10 for row in M for col in row])  # [11,12,13,14,15,16]
    print('')
    res = []
    for row in M:
        for col in row:
            res.append(col + 10)
    print(res)  # [11,12,13,14,15,16,17,18,19]
    print('')

    # [1,2,3,4,5,6,7,8,9]
    print([M[row][col] for row in range(len(M)) for col in range(len(M[row]))])
    print('')

    # NOTE: for nested list comprehensions over a multi-dimensional data
    # structure, the right most loop is the outer loop and the left most loop
    # is the inner loop
    # [[1,2,3],[4,5,6],[7,8,9]]
    print([[M[row][col] for col in range(len(M[row]))]
           for row in range(len(M))])
    print('')

    print([[col + 10 for col in row] for row in M])  # [[11,12,13],[14,15,16]]
    print('')

    res = []
    for i in range(len(M)):
        res.append([])
        for j in range(len(M[i])):
            res[i].append(M[i][j] + 10)
    print(res)  # [[11,12,13],[14,15,16]]
    print('')

    res = []
    for row in M:
        tmp = []
        for col in row:
            tmp.append(col + 10)
        res.append(tmp)  # [[11,12,13],[14,15,16]]
    print(res)
    print('')

    # pair-wise multiplication of corresponding elements
    # [2,4,6,12,15,18,28,32,36]
    print([M[row][col] * N[row][col] for row in range(3) for col in range(3)])
    print('')
    
    # [[2,4,6],[12,15,18],[28,32,36]]
    print([[M[row][col] * N[row][col] for col in range(3)]
           for row in range(3)])
    print('')

    res = []
    for row in range(3):
        tmp = []
        for col in range(3):
            tmp.append(M[row][col] * N[row][col])
        res.append(tmp)
    print(res)  # [[2,4,6],[12,15,18],[28,32,36]]
    print('')

    # same as ^^^ using zip()
    # [[2,4,6],[12,15,18],[28,32,36]]
    print([[col1 * col2 for (col1, col2) in zip(row1, row2)]
          for (row1, row2) in zip(M, N)])
    print('')

    # same as ^^^ using zip() in a loop
    res = []
    for (row1, row2) in zip(M, N):
        tmp = []
        for (col1, col2) in zip(row1, row2):
            tmp.append(col1 * col2)
        res.append(tmp)
    print(res)  # [[2,4,6],[12,15,18],[28,32,36]]
