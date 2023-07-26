if __name__ == '__main__':
    print('code snippets from page 1149\n')

    try:
        1 / 0
    except Exception as E:
        raise TypeError('Bad') from E  # explicitly chained exceptions
