if __name__ == '__main__':
    print('code snippets from pages 268-269\n')
    Matrix = {}  # empty dictionary
    # hypothetical 3D array
    # use keys as coordinates that have some associated value
    Matrix[(2, 3, 4)] = 88
    Matrix[(7, 8, 9)] = 99
    print(Matrix)

    X = 2
    Y = 3
    Z = 4
    print(Matrix[(X, Y, Z)])  # 88
