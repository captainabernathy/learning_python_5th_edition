# usage: python3 list_comprehensions_first_look.py

if __name__ == '__main__':
    print('code snippets from pages 441-442\n')

    L = [1, 2, 3, 4]

    print(L)  # [1,2,3,4]

    # iterate and add 10 to every element in the list
    for i in range(len(L)):
        L[i] += 10
    print(L)  # [11,12,13,14]
    print('')

    # same as ^^ with list comprehension
    L = [1, 2, 3, 4]

    # NOTE: remember to enclose list comprehensions with brackets or use the
    # list() constructor
    L = [x + 10 for x in L]

    print(L)  # [11,12,13,14]

    print(list(x + 10 for x in L))  # [21,22,23,24]
    print('')
    
    L = [1, 2, 3, 4]

    # similarly, use a list object's append() method to build up a list
    res = []
    for x in L:
        res.append(x + 10)

    print(res)  # [11,12,13,14]
