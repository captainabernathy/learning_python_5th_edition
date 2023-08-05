# usage: python3 mapping_functions_over_iterables_via_map.py

# function returns the sum of its argument and 10
def inc(x):
    return x + 10


# function calls the func passed to fun on every element in seq and returns
# a list that contains the result
def mymap(func, seq):
    res = []
    for x in seq:
        res.append(func(x))
    return res


if __name__ == '__main__':
    print('code snippets from pages 597-598\n')

    counters = [1, 2, 3, 4]
    print(counters)  # [1,2,3,4]
    print('')

    updated = []
    for x in counters:
        updated.append(x + 10)

    print(updated)  # [11,12,13,14]
    print('')

    # NOTE: map() applies a function to the items in an iterable

    # call the function inc() on each element in the list counters and return
    # the result in a list
    print(list(map(inc, counters)))  # [11,12,13,14]
    print('')

    # call a lambda function on each element in the list counters and return
    # the result in a list
    print(list(map((lambda x: x + 3), counters)))  # [4,5,6,7]
    print('')

    # call the funcion inc() on each element in the provided list and return
    # the result in a list
    print(list(map(inc, [1, 2, 3])))  # [11,12,13]
    print('')

    # mymap() calls the function inc() on each element of the provided list
    # and returns a list containing the result
    print(mymap(inc, [1, 2, 3]))
    print('')

    print(pow(3, 4))  # 81... 3 ** 4
    print('')

    # call the function pow(a,b) on the corresponding elements of the two
    # lists provided and return the results in a list
    print(list(map(pow, [1, 2, 3], [2, 3, 4])))  # [1,8,81]... 1**2, 2**3, 3**4
    print('')

    print(list(map(inc, [1, 2, 3, 4])))  # [11,12,13,14]
    print('')

    # same as ^^^ but with a list comprehension
    print([inc(x) for x in [1, 2, 3, 4]])  # [11,12,13,14]
