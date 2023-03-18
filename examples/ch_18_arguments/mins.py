# function returns the minimum element from any number of positional arguments
# for any type that supports less than comparisons
def min1(*args):
    # NOTE: if called with no arguments the attempt to access args[0] will
    # raise an exception
    res = args[0]  # assume first argument is the minimum
    for arg in args[1:]:  # loop over the rest of the elements
        if arg < res:  # update current minimum when the current element is
            res = arg  # less than the current minimum
    return res  # return minimum


# function returns the minimum element from the arguments passed to it
def min2(first, *rest):
    # assume first is the minimum
    for arg in rest:  # loop over the rest of the arguments
        # NOTE: if the arguments being compared are not of the same type, the
        # comparison will raise an exception
        if arg < first:  # update the current minimum when the current element
            first = arg  # is less than the current minimum
    return first  # return minimum


# function returns the minimum element from any number of positional arguments
# for any type that supports less than comparisons
def min3(*args):
    # convert all arguments received into a list
    tmp = list(args)  # or, in python 2.4+: return sorted(args)[0]
    # sort the list
    tmp.sort()
    # NOTE: if called with no arguments the attempt to access tmp[0] will
    # raise an exception
    return tmp[0]  # return first element in list since it is the minimum


if __name__ == '__main__':
    print('code snippets from page 564\n')
    print(min1(3, 4, 1, 2))  # 1
    print(min2("bb", "aa"))  # aa
    print(min3([2, 2], [1, 1], [3, 3]))  # [1,1]
