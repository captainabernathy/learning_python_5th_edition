import docstr

if __name__ == '__main__':
    print('code snippets from pages 911-912\n')

    print('x' * 40)
    print(docstr.__doc__)

    print('x' * 40)
    print(docstr.func.__doc__)

    print('x' * 40)
    print(docstr.spam.__doc__)

    print('x' * 40)
    print(docstr.spam.method.__doc__)

    print('x' * 40)
    X = docstr.spam()
    X.method()

    print('x' * 40)
