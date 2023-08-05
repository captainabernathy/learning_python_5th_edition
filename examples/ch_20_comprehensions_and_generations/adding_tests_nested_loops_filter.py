# usage: python3 adding_tests_nested_loops_filter.py

if __name__ == '__main__':
    print('code snippets from pages 605-606\n')

    # list comprehension that returns the even numbers in [0,4]
    print([x for x in range(5) if not x % 2])  # [0,2,4]

    # NOTE: filter() applies a test to an iterable and returns the results that
    # evaluate to True
    # Here, lambda: x not x % 2, range 5 => [True,False,True,False,True]
    # applying filter() to ^^^ => [0,2,4]
    print(list(filter(lambda x: not x % 2, range(5))))  # [0,2,4]

    # same as above but using the loop and appending the results in a list
    res = []
    for x in range(5):
        if not x % 2:
            res.append(x)
    print('')

    # list comprehension that returns the square of the even numbers in [0-9]
    print([x ** 2 for x in range(10) if not x % 2])  # [0,4,16,36,64]

    # square the result of the even numbers between [0-9]
    print(list(map(lambda x: x ** 2, filter(lambda x: not x % 2, range(10)))))
