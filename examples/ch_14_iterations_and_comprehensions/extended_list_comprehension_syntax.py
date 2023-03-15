if __name__ == '__main__':
    print('code snippets from pages 444-445\n')

    # remove trailing whitespace for all lines the begin with 'p'
    lines = [line.rstrip() for line in open('script2.py') if line[0] == 'p']
    print(lines)
    print('')

    # same as ^^^
    res = []
    for line in open('script2.py'):
        if line and line[0] == 'p':
            res.append(line.rstrip())
    print(res)
    print('')

    # remove trailing whitespace for all lines in a file that end with a digit
    print([line.rstrip() for line in open('script2.py')
           if line.rstrip()[-1].isdigit()])
    print('')

    # concatenate each letter in 'abc' to each letter in 'lmn'
    print([x + y for x in 'abc' for y in 'lmn'])  # ['al','am','an',...,'cn']
    print('')

    # similarly...
    res = []
    for x in 'abc':
        for y in 'lmn':
            res.append(x + y)
    print(res)
