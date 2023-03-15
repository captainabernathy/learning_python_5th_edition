if __name__ == '__main__':
    print('code snippets from pages 433-434\n')
    L = [1, 2, 3]
    # NOTE: the iter() function returns an iterator object from an iterable
    It = iter(L)
    print(It.__next__())  # 1
    print(It.__next__())  # 2
    print(It.__next__())  # 3
    print('')
    
    # iterating over list using __next__()
    It = iter(L)
    try:
        while True:
            print(It.__next__())
    except StopIteration:
        pass
    print('')

    # NOTE: a file object is its own iterable
    f = open('script2.py')
    print(iter(f) is f)  # True
    print(iter(f) is f.__iter__())  # True
    print(f.__next__())
    f.close()

    # NOTE: not all objects are their own iterators
    print(iter(L) is L)  # false
    try:
        L.__next__()  # list has no __next__() method
    except AttributeError as ex:
        print(ex)
    print('')

    It = iter(L)
    print(It.__next__())
    print(next(It))  # same as I.__next__()
    print('')

    # iterating over a list using next()
    It = iter(L)
    try:
        while True:
            print(next(It))
    except StopIteration:
        pass
    print('')

