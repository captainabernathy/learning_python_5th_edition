if __name__ == '__main__':
    print('code snippets from pages 402-403\n')
    x = 'spam'
    while x:
        print(x, end=' ')  # spam pam am m
        x = x[1:]  # strip off first character
    print('')

    a = 0
    b = 10
    while a < b:
        print(a, end=' ')  # 0 1 2 3 4 5 6 7 8 9
        a += 1
    print('')
