# class that demonstrates how to overload the __getitem__() method
class Indexer:
    # NOTE: the an object's __getitem__() method an indexing operation is
    # performed
    def __getitem__(self, index):
        return index ** 2


if __name__ == '__main__':
    print('code snippets from page 919\n')
    X = Indexer()
    print(X[2])  # 4
    print('')

    for i in range(5):
        print(X[i], end=' ')  # 0 1 4 9 16
    print('')
