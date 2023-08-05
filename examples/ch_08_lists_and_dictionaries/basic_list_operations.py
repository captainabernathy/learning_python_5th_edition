# usage: python3 basic_list_operations.py

if __name__ == '__main__':
    print('code snippets from page 250\n')

    # basic list operations

    # length
    print(len([1, 2, 3]))  # 3

    # concatenation... returns a new list
    print([1, 2, 3] + [4, 5, 6])  # [1,2,3,4,5,6]

    # repetition
    print(['Ni'] * 4)  # ['Ni','Ni','Ni','Ni']

    # NOTE: to contacenate a list and a string you must first either

    # convert the list to a string, or...
    print(str([1, 2]) + '34')  # '[1, 2]34'

    # convert the string to a list
    print([1, 2] + list("34"))  # [1,2,'3','4']
