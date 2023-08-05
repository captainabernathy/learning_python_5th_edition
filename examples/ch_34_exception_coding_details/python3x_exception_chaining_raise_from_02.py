# usage: python3 python3x_exception_chaining_raise_from_02.py

if __name__ == '__main__':
    print('code snippets from page 1150\n')

    try:
        1 / 0
    except:
        badname  # not defined => implicitly chained exception
