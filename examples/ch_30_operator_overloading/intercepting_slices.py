# class that demonstrates how to overload the __getitem__() method
class Indexer_01:
    data = [5, 6, 7, 8, 9]  # class data

    # overloads indexing operator... returns self.data[index]
    def __getitem__(self, index):  # called for index or slice
        print('getitem:', index)
        return self.data[index]  # performs index or slice


class Indexer_02:
    # NOTE: when appropriate the __getitem__() method can test its argument
    # and extract slice object bounds
    def __getitem__(self, index):
        if isinstance(index, int):  # test usage
            print('indexing', index)
        else:
            print('slicing', index.start, index.stop, index.step)


if __name__ == '__main__':
    print('code snippets from pages 919-921\n')

    L = [5, 6, 7, 8, 9]
    print(L[2:4])  # [7,8]... elements 2 and 3
    print(L[1:])   # [6,7,8,9]... second element to the end
    print(L[:-1])  # [5,6,7,8]... all but the last element
    print(L[::2])  # [5,7,9]... every other element
    print('')

    # indexing with slice objects
    print(L[slice(2, 4)])  # same as L[2:4]
    print(L[slice(1, None)])  # from index 1 to end... same as L[1:]
    print(L[slice(None, -1)])  # all but the last element... same as L[:-1]
    print(L[slice(None, None, 2)])  # same as... L[::2]
    print('')

    X = Indexer_01()
    print(X[0])  # 5
    print(Indexer_01.__getitem__(X, 0))  # 5... same as ^^^
    print(X[1])  # 6
    print(X[-1])  # 9... last item
    print('')

    # slicing sends __getitem__() a slice object
    print(X[2:4])  # [7,8]
    print(X[1:])  # [6,7,8,9]
    print(X[:-1])  # [5,6,7,8]
    print(X[::2])  # [5,7,9]
    print('')

    X = Indexer_02()
    X[99]  # indexing 99
    X[1:99:2]  # slicing 1 99 2
    X[1:]  # slicing 1 None None
