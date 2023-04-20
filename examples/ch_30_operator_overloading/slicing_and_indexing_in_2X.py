# NOTE: python 2.X classes can also define the __getslice__() and
# __setslice__() methods to get/set objects by slice objects
class Slicer:
    # overloads indexing operations
    def __getitem__(self, index):
        print index

    # overloads reading by slice
    def __getslice__(self, i, j):
        print i, j

    def __setslice__(self, i, j, seq):
        print 'hey'
        print i, j, seq


if __name__ == '__main__':
    print('code snippets from pages 921-922\n')
    Slicer()[1]  # 1... runs __getitem__() with int... like 3.X
    Slicer()[1:9]  # 1 9... runs __getslice__() if present, else __getitem__
    Slicer()[1:9:2]  # runs __getitem__() with slice()... like 3.X

