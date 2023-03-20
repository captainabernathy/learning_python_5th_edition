# function recursively computes the sum of an arbitrarily nested list of
# numbers and returns the results
def sumtree(L):
    tot = 0
    for x in L:  # scan L
        if not isinstance(x, list):
            tot += x  # add directly
        else:
            tot += sumtree(x)  # recur for sublists
    return tot


if __name__ == '__main__':
    print('code snippets from page 581\n')
    L = [1, [2, [3, 4], 5], 6, [7, 8]]  # arbitrarily nested list
    print(sumtree(L))  # 36

    # pathological cases
    print(sumtree([1, [2, [3, [4, [5]]]]]))  # 15... right-heavy
    print(sumtree([[[[[1], 2], 3], 4], 5]))  # 15... left-heavy
