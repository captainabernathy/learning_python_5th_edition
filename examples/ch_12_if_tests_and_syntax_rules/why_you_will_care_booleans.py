if __name__ == '__main__':
    L = [1, 0, 2, 0, 'spam', '', 'ham', []]
    print(L)  # [1, 0, 2, 0, 'spam', '', 'ham', []]
    print('')

    # use the filter() function to get true values from list
    print(list(filter(bool, L)))  # [1,2,spam,ham]
    # same as ^^^ via comprehension
    print([x for x in L if x])  # [1,2,spam,ham]
    print('')

    # use the any() and all() functions to determine aggregrate truth values
    print(any(L), all(L))  # True False
