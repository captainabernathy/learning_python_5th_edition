# usage: python3 sequence_operations_lists.py

if __name__ == '__main__':
    print('code snippets from pages 111-112\n')

    # create a list
    L = [123, 'spam', 1.23]
    print(L)

    # len() shows the number of items in a list
    print(len(L))  # 3

    # indexing by position
    print(L[0])  # 123

    # slicing returns a new list
    print(L[:-1])  # [123, 'spam']

    # use + for list concatenation
    print(L + [4, 5, 6])

    # use * to concatenate a copy of the list to itself
    print(L * 2)

    # the original list was not changed
    print(L)
