if __name__ == '__main__':
    print('code snippets from page 112\n')
    L = [123, 'spam', 1.23]
    print(L)

    # use the append() method to add to the end of the list
    L.append('NI')
    print(L)

    # use pop() to delete an item at a specific position
    L.pop(2)
    print(L)

    # alternatively use the del() function
    del L[2]
    print(L)

    M = ['bb', 'aa', 'cc']
    print(M)

    # the sort() function method sorts the list in place
    M.sort()
    print(M)

    # the reverse() function reverses the list in place
    M.reverse()
    print(M)
