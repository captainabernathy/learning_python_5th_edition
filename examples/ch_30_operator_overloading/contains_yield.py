from __future__ import print_function  # for 2.X/3.X interoperability


class Iters:
    # initializes this Iters's data attribute to value
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):  # fallback for iteration, index, slice
        print('get[%s]:' % i, end='')
        return self.data[i]

    # yeilds the next element when iterating over this Iters
    # NOTE: this Iters's __iter__() employs yield, which allows for  multiple
    # active scans
    def __iter__(self):  # preferred for iteration
        print('iter=> next:', end='')  # allows multiple active iterators
        for x in self.data:
            yield x
            print('next:', end='')

    def __contains__(self, x):  # preferred for 'in'
        print('contains: ', end='')
        return x in self.data


if __name__ == '__main__':
    print('code snippets from pages 936-937\n')
    X = Iters([1, 2, 3, 4, 5])
    print(3 in X)  # contains: True
    print('')

    for i in X:
        # iter=> next:1 | next:2 | next:3 | next:4 | next:5 | next:
        print(i, end=' | ')
    print('\n')

    # iter=> next:next:next:next:next:next:[1, 4, 9, 16, 25]
    print([i ** 2 for i in X])
    print('')

    # iter=>next:next:next:next:next:next:['0b1','0b10','0b11','0b100','0b101']
    print(list(map(bin, X)))
    print('')

    It = iter(X)  # manual iteration (what other contexts do)
    try:
        # iter=>next:1 @ next:2 @ next:3 @ next:4 @ next:5 @ next:StopIteration
        while True:
            print(next(It), end=' @ ')
    except StopIteration:
        print('StopIteration')
