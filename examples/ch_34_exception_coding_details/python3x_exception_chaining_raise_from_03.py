if __name__ == '__main__':
    print('code snippets from page 1150\n')

    # explicit chaining
    try:
        try:
            raise IndexError()
        except Exception as E:
            raise TypeError() from E
    except Exception as E:
        raise SyntaxError() from E
