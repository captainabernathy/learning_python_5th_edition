if __name__ == '__main__':
    print('code snippets from pages 251-252\n')
    L = ['spam', 'Spam', 'SPAM!']
    print(L)  # ['spam', 'Spam', 'SPAM!']
    print(L[2])   # offset starts at 0... SPAM!
    print(L[-2])  # negative count from right... spam

    # NOTE: slicing returns a new list
    print(L[1:])  # slicing... from element 1 to end... ['Spam','SPAM!']
    print('')

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrix[1])  # second row... [4,5,6]
    print(matrix[1][1])  # second row, second element... 5
    print(matrix[2][0])  # third row, first element... 7
