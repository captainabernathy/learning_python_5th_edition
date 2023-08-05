# usage: python3 scopes_and_try_except_variables_3x.py

if __name__ == '__main__':
    print('code snippets from pages 1147-1148\n')

    # try:
    #     1 / 0
    # except Exception, X:  # invalid syntax in 3.X
    #     print(X)
    # print('')

    try:
        1 / 0
    except Exception as X:  # 3.X localizes as names to the try block, so...
        print(X)  # division by zero
    print('')

    try:
        print(X)  # X is not defined
    except Exception as X:
        print(X)  # name 'X' is not defined
    print('')

    # NOTE: variables defined with an as clause are removed after the except
    # statement, so...
    X = 99
    try:
        1 / 0
    except Exception as X:
        print(X)  # division by zero
    print('')

    try:
        print(X)  # X has been undefined here
    except Exception as ex:
        print(ex)  # name 'X' is not defined
    print('')

    # this behavior is the opposite standard comprehension behavior, where
    # external references are retained following the comprehension
    X = 99
    print([X for X in 'spam'])  # ['s','p','a','m']
    print(X)  # 99
    print('')

    # If you need to reference the exception instance after the try statement,
    # assign it to another name so it won't be automatically removed
    try:
        1 / 0
    except Exception as X:
        print(X)  # division by zero
        saved = X
    print('')

    print(saved)  # division by zero
