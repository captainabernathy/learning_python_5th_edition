print('I am:', __name__)


# function determines the minimum or maximum element in args as determeined by
# the function handle passed to test and returns that element
def minmax(test, *args):
    res = args[0]  # assume first element is min/max element
    for arg in args[1:]:  # loop over the rest of the arguments
        if test(arg, res):   # apply test and update current min/max based on
            res = arg        # the result
    return res  # return result


# returns the result of testing whether x is less than y
def lt(x, y):
    return x < y


# returns the result of testing whether x is greater than y
def gt(x, y):
    return x > y


if __name__ == "__main__":
    print('code snippets from pages 773-774\n')

    print(minmax(lt, 4, 2, 1, 5, 6, 3))  # 1
    print(minmax(gt, 4, 2, 1, 5, 6, 3))  # 6
