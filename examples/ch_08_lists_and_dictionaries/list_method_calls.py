if __name__ == '__main__':
    print('code snippets from pages 254-255\n')
    L = ['eat', 'more', 'SPAM!']
    print(L)  # ['eat', 'more', 'SPAM!']
    print('')

    # NOTE: a list's append method inserts a single iterable element at
    # the end of this list
    L.append('please')
    print(L)  # ['eat', 'more', 'SPAM!', 'please']
    print('')

    # NOTE: capital letters have a lower numeric value than lowercase letters
    L.sort()  # the a list's sort() method sorts its elements in place
    print(L)  # ['SPAM!','eat','more','please']
