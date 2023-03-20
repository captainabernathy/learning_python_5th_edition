trace = (lambda x: None)  # or print()
visit = (lambda x: print(x, end=', '))


# function computes the sum of an arbitrarily nested list of numbers via
# breadth-first traversal by item
# breadth-first by items... add to end
def bf_sumtree(L):  # breadth-first, explicit queue
    tot = 0
    items = list(L)  # top-level copy
    while items:
        trace(items)
        front = items.pop(0)  # remove the first item
        if not isinstance(front, list):
            tot += front  # add numbers directly
            visit(front)
        else:
            items.extend(front)  # append nested list
    return tot


# function computes the sum of an arbitrarily nested list of numbers via
# depth-first traversal by item
# depth-first by items: add to front (like recursive calls versions)
def df_sumtree(L):  # depth-first, explicit stack
    tot = 0
    items = list(L)  # top-level copy
    while items:
        trace(items)
        front = items.pop(0)  # remove the first item
        if not isinstance(front, list):
            tot += front
            visit(front)
        else:
            items[:0] = front  # prepend nested list
    return tot


# function computes the sum of an arbitrarily nested list of numbers via
# breadth-first traversal by level
# breadth-first by levels
def bfl_sumtree(L):
    tot = 0
    levels = [L]  # wrap L
    while levels:
        trace(levels)
        front = levels.pop(0)  # remove the first level
        for x in front:
            if not isinstance(x, list):
                tot += x
                visit(x)
            else:
                levels.append(x)  # push nested list
    return tot


if __name__ == '__main__':
    print('code snippets from pages 578-580\n')
    L = [1, [2, [3, 4], 5], 6, [7, 8]]
    s = bf_sumtree(L)  # 1, 6, 2, 5, 7, 8, 3, 4
    print('')
    print(s)  # 36

    # pathological cases
    s = bf_sumtree([1, [2, [3, [4, [5]]]]])  # 1, 2, 3, 4, 5 right-heavy
    print('')
    print(s)  # 15
    s = bf_sumtree([[[[[1], 2], 3], 4], 5])  # 5, 4, 3, 2, 1 left-heavy
    print('')
    print(s)  # 15
    print('')

    L = [1, [2, [3, 4], 5], 6, [7, 8]]
    s = df_sumtree(L)  # 1, 2, 3, 4, 5, 6, 7, 8
    print('')
    print(s)  # 36

    # pathological cases
    s = df_sumtree([1, [2, [3, [4, [5]]]]])  # 1, 2, 3, 4, 5  right-heavy
    print('')
    print(s)  # 15
    s = df_sumtree([[[[[1], 2], 3], 4], 5])  # 1, 2, 3, 4, 5 left-heavy
    print('')
    print(s)  # 15
    print('')

    L = [1, [2, [3, 4], 5], 6, [7, 8]]
    s = bfl_sumtree(L)  # 1, 6, 2, 5, 7, 8, 3, 4
    print('')
    print(s)  # 36

    # pathological cases
    s = bfl_sumtree([1, [2, [3, [4, [5]]]]])  # 1, 2, 3, 4, 5 right-heavy
    print('')
    print(s)
    s = bfl_sumtree([[[[[1], 2], 3], 4], 5])  # 5, 4, 3, 2, 1 left-heavy
    print(s)
