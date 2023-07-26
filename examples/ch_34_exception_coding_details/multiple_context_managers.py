if __name__ == '__main__':
    print('code snippets from pages 1157-1158\n')

    # parallelline scan of two files
    with open('script1.py') as f1, open('script2.py') as f2:
        for pair in zip(f1, f2):
            print(pair)
    print('')

    with open('script1.py') as f1, open('script2.py') as f2:
        for (linenum, (line1, line2)) in enumerate(zip(f1, f2)):
            if line1 != line2:
                print('%s\n%r\n%r' % (linenum, line1, line2))
    print('')

    # same as first example in CPython... same effect as auto close
    for pair in zip(open('script1.py'), open('script2.py')):
        print(pair)
    print('')

    # PyPy and Jython may require more direct closure inside loops to avoid
    # taxing system resources
    # this example closes the output file on statement exit to ensure that any
    # buffered text is transferred to disk immediately
    with open('script2.py') as fin, open('upper1.txt', 'w') as fout:
        for line in fin:
            fout.write(line.upper())

    print(open('upper1.txt').read())

    # Alternatively
    fin = open('script2.py')
    fout = open('upper2.txt', 'w')
    for line in fin:  # same effect as before, auto close
        fout.write(line.upper())
    
    fout.close()  # explicitly close output file so that buffered text is
                  # flushed to disk

    print(open('upper2.txt').read())

    # in cases where programs must continue after exceptions, the 'with' forms
    # also implicitly catch exceptions... and also avoid try/finally in cases
    # where close is required

    # explicit implementation of ^^^
    fin = open('script2.py')
    fout = open('upper3.txt', 'w')
    try:  # same as before but with explicit close on error
        for line in fin:
            fout.write(line.upper())
    finally:
        fin.close()
        fout.close()

    print(open('upper3.txt').read())
