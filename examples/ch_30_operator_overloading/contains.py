from __future__ import print_function  # for 2.X/3.X interoperability


class Iters:
    # initializes this Iters's data attribute to value
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):  # fallback for iteration, index, slice
        print('get[%s]:' % i, end='')
        return self.data[i]

    # NOTE: this Iters's __iter__() supports multiple scans... BUT only a
    # single scan can be active at any point in time... SO nested loops won't
    # work
    def __iter__(self):  # preferred for iteration...
        print('iter=> ', end='')  # allows only 1 active iterator
        self.ix = 0
        return self

    # complements __iter__()
    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, x):  # preferred method for "in" operator
        print('contains: ', end='')
        return x in self.data

    next = __next__  # 2.X/3.X compatibility


if __name__ == '__main__':
    print('code snippets from pages 935-936\n')
    X = Iters([1, 2, 3, 4, 5])  # make instances
    print(3 in X)  # contains: True... membership
    print('')

    for i in X:
        # iter=> next:1 | next:2 | next:3 | next:4 | next:
        print(i, end=' | ')
    print('\n')

    # iter=> next:next:next:next:next:next:[1,4,9,16,25]
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
