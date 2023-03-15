if __name__ == '__main__':
    print('code snippets from pages 433-434\n')

    # read the whole file at once
    print(open('script2.py').read())

    # NOTE: open returns a file object
    f = open('script2.py')
    # a file object's readline() method reads a single line from a file
    # NOTE: readline() returns an empty string at EOF
    print(f.readline(), end='')
    print(f.readline(), end='')
    print(f.readline(), end='')
    print(f.readline(), end='')
    f.close()  # remember to close open file handle
    print('')

    f = open('script2.py')
    # NOTE: a file object's __next__() method also reads a single line from a
    # file, but it raises a StopIteration exception at EOF
    print(f.__next__(), end='')
    print(f.__next__(), end='')
    print(f.__next__(), end='')
    print(f.__next__(), end='')
    f.close()
    print('')

    # use file iterators to read a file line by line
    # NOTE: file handles are auto-closed when they opened within an iteration
    # context
    for line in open('script2.py'):
        print(line.upper(), end='')
    print('')

    # calling readlines() within an iteration context can also be used to
    # read a file line by line
    for line in open('script2.py').readlines():  # older way to do ^^^
        print(line.upper(), end='')
    print('')

    # NOTE: when reading a file within a while loop, remember to close() it
    f = open('script2.py')
    while True:
        line = f.readline()
        if not line:
            break
        print(line.upper(), end='')
    f.close()
