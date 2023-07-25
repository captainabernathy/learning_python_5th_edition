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
            print(It.__next__())  # 1 2 3
    except StopIteration:
        pass
    print('')

    # NOTE: a file object is its own iterable
    f = open('script2.py')
    print(iter(f) is f)  # True
    print(iter(f) is f.__iter__())  # True
    print(f.__next__())  # import sys... first line in script2.py
    f.close()

    # NOTE: not all objects are their own iterators
    print(iter(L) is L)  # false
    try:
        L.__next__()
    except AttributeError as ex:
        print(ex)  # list has no __next__() method
    print('')

    It = iter(L)
    print(It.__next__())  # 1
    print(next(It))  # 2... same as I.__next__()
    print('')

    # iterating over a list using next()
    It = iter(L)
    try:
        while True:
            print(next(It))  # 1 2 3
    except StopIteration:
        pass
    print('')
