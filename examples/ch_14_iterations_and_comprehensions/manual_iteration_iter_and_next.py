# usage: python3 manual_iteration_iter_and_next.py

if __name__ == '__main__':
    print('code snippets from page 435\n')

    myfile = 'script2.py'
    f = open(myfile)

    # NOTE: a file object's __next__() method reads a single line from a
    # file and raises a StopIteration exception at EOF
    print(f.__next__(), end='')  # call iteration method directly
    print(f.__next__(), end='')
    f.close()
    print('')

    f = open(myfile)

    # NOTE: In python 3.X, when given an iterator object, the next(f) function
    # performs the same as f.__next__() in 3.X and f.next() in 2.X
    print(next(f), end='')  # next(f) built-in calls f.__next__() in 3.X
    print(next(f), end='')
    f.close()
