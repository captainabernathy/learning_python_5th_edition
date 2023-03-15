if __name__ == '__main__':
    print('code snippets from pages 418-419\n')
    X = 'spam'
    print(X)  # spam
    print(len(X))  # 4
    print(list(range(len(X))))  # [0,1,2,3]
    print('')

    for item in X:
        print(item, end=' ')  # s p a m
    print('')

    # similarly...
    i = 0
    while i < len(X):
        print(X[i], end=' ')  # s p a m
        i += 1
    print('')

    # alternatively
    for i in range(len(X)):
        print(X[i], end=' ')  # s p a m
    print('')
