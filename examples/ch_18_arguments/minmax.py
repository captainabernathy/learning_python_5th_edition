# function determines the minimum or maximum element in args as determeined by
# the function handle passed to test and returns that element
def minmax(test, *args):
    res = args[0]  # assume first element is the min/max element
    for arg in args[1:]:  # loop over the rest of the arguments
        if test(arg, res):  # apply test and update current min/max based on
            res = arg       # result
    return res  # return result


# function returns the result of testing whether x is less than y
def lt(x, y):
    return x < y


# function returns the result of testing whether x is greater than y
def gt(x, y):
    return x > y


if __name__ == '__main__':
    print('code snippets from page 565\n')
    print(minmax(lt, 4, 2, 1, 5, 6, 3))  # 1
    print(minmax(gt, 4, 2, 1, 5, 6, 3))  # 6
