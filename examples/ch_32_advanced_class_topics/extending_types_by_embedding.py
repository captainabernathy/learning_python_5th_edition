# program demonstrates how to use the setwrapper module's Set class

from setwrapper import Set


if __name__ == '__main__':
    print('code snippets from pages 1014-1015\n')

    x = Set([1, 3, 5, 7])  # build a set
    print(x)  # Set: [1,3,5,7]
    print(x.union(Set([1, 4, 7])))  # Set: [1,3,5,7,4]... set union
    print(x | Set([1, 4, 6]))  # Set: [1,3,5,7,4,6]... also set union

