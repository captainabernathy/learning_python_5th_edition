if __name__ == '__main__':
    print('code snippets from pages 421-422\n')
    L = [1, 2, 3, 4, 5]
    print(L)  # [1, 2, 3, 4, 5]

    for x in L:
        x += 1  # changes x NOT L
    print(L)  # [1, 2, 3, 4, 5]

    for i in range(len(L)):
        L[i] += 1  # changes L
    print(L)  # [2, 3, 4, 5, 6]

    i = 0
    while i < len(L):
        L[i] += 1  # changes L
        i += 1
    print(L)  # [3,4,5,6,7]
