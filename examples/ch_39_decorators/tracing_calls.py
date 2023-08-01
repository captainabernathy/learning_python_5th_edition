from decorator1 import spam


if __name__ == '__main__':
    print('code snippets from pages 1328-1329\n')

    spam(1, 2, 3)  # call 1 to spam... 6
    print('')

    spam('a', 'b', 'c')  # call 2 to spam... abc
    print('')

    print(spam.calls)  # 2
    print('')

    print(spam)  # <decorator1.tracer object at 0x...>
    print('')
