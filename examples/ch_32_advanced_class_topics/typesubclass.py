# usage: python3 typesubclass.py

# program implements a class that extends python's list class so that it
# supports one-based indexing via __getitem__() and demonstrates its usage

# class that extends python's list class by overloading its __getitem__()
# operator to provide one-based (as opposed to zero-based) indexing
class MyList(list):

    # enables this MyList object to use one-based indexing by returning the
    # element at position idx - 1
    def __getitem__(self, idx):
        print('(indexing %s at %s)' % (self, idx))
        return list.__getitem__(self, idx - 1)


if __name__ == '__main__':
    print('code snippets from pages 1015-1016\n')

    print(list('abc'))  # ['a','b','c']
    x = MyList('abc')  # inherits __init__() from list
    print(x)  # ['a','b','c']... inherits __repr__() from list
    print('')

    print(x[1])  # a
    print(x[2])  # b
    print(x[3])  # c
    print('')

    x.append('spam')  # inherits append() method from list
    print(x)  # ['a','b','c','spam']
    x.reverse()  # inherits reverse() method from list
    print(x)  # ['spam','a','b','c']
