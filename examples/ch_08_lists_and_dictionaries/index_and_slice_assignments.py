if __name__ == '__main__':
    print('code snippets from pages 252-254\n')
    L = ['spam', 'Spam', 'SPAM!']
    print(L)  # ['spam', 'Spam', 'SPAM!']
    print('')

    L[1] = 'eggs'  # overwrite second element
    print(L)  # ['spam', 'eggs', 'SPAM!']
    print('')

    # slice assignments
    # NOTE: only an iterable can be assigned to an iterable
    # delete elements 0 and 1, insert two elements at position 0
    L[0:2] = ['eat', 'more']
    print(L)  # ['eat', 'more', 'SPAM!']
    print('')

    L = [1, 2, 3]
    print(L)  # [1,2,3]
    print('')

    # delete element at position 1, insert two elements at position 1
    L[1:2] = [4, 5]  # first element,
    print(L)  # [1,4,5,3]
    print('')

    # NOTE: var[n:n] returns an empty list, so...
    # var[n:n] = [x] ... inserts x after element n in var
    L[1:1] = [6, 7]  # insertion after first element
    print(L)  # [1,6,7,4,5,3]
    print('')

    # delete element at position 1
    L[1:2] = []  # deletion
    print(L)  # [1,7,4,5,3]
    print('')

    # assignment to a new list
    L = [1]
    print(L)  # [1]
    print('')

    # NOTE: var[:0] returns at empty list, so...
    # var[:0] = [x]... inserts x at the beginning... before element 0... in var
    L[:0] = [2, 3, 4]  # insert at the beginning
    print(L)  # [2,3,4,1]
    print('')

    # NOTE: var[len(var):] returns an empty list, so...
    # var[len(var):] = [x]... inserts x at the end... after the last element in
    # var
    L[len(L):] = [5, 6, 7]  # insert at end
    print(L)  # [2,3,4,1,5,6,7]
    print('')

    # a list's extend() method inserts the elements of iterable at the end of
    # this list
    L.extend([8, 9, 10])  # insert all at end
    print(L)  # [2,3,4,1,5,6,7,8,9,10]
