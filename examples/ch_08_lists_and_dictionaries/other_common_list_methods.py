if __name__ == '__main__':
    print('code snippets from pages 257-258\n')
    L = [1, 2]
    print(L)  # [1, 2]

    # a list's extend() method inserts the elements of iterable at the end of
    # this list
    L.extend([3, 4, 5])  # add to end
    print(L)  # [1,2,3,4,5]
    print('')

    # a list's pop() method removes and returns the last element in this list
    print(L.pop())  # remove and return last element... 5
    print(L)  # [1,2,3,4]
    print('')

    # a list's reverse() method reverses the order of the elements in this list
    # in place
    L.reverse()
    print(L)  # [4,3,2,1]

    # NOTE: the reverse function returns a new list that contains the elements
    # of the list it received in reverse order... it does not change its
    # argument in place
    print(list(reversed(L)))  # [1,2,3,4]
    print(L)  # [4,3,2,1]... L not changed
    print('')

    L = []  # empty list
    L.append(1)
    L.append(2)
    print(L)  # [1,2]
    print(L.pop())  # 2
    print(L)  # [1]
    print('')

    L = ['spam', 'eggs', 'ham']
    print(L)  # ['spam', 'eggs', 'ham']

    # a list's index method returns the index of an element in this list
    print(L.index('eggs'))  # return index of object
    print('')

    # a list's insert() method inserts an element in this list at the specified
    # index and extends the list by 1
    L.insert(1, 'toast')  # insert at position
    print(L)  # ['spam', 'toast','eggs', 'ham']

    # a list's remove() element removes the specified element in this list
    # and decreases the lenght of the list by 1
    L.remove('eggs')  # delete by value
    print(L)  # ['spam', toast', 'ham']

    # NOTE: when provided an index, a list's pop() method will remove and 
    # return the element at that index in this list and decrease the list's 
    # length by 1
    print(L.pop(1))  # delete by position
    print(L)  # ['spam', 'ham']

    # a list's count() method will return the number of times the argument it
    # receives occurs in this list
    print(L.count('spam'))  # number of occurrences
