# usage: python(2/3) skipper_2x.py

from __future__ import print_function  # for 2.X/3.X interoperability


class SkipObject:
    def __init__(self, wrapped):  # save item to be used
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterator(self.wrapped)  # new SkipIterator each call


class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped  # iterator state information
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):  # terminate iterations
            raise StopIteration
        else:
            item = self.wrapped[self.offset]  # else return and skip...
            self.offset += 2
            return item

    next = __next__  # 2.X/3.X compatibility


if __name__ == '__main__':
    print('code snippets from pages 928-930\n')

    alpha = 'abcdef'
    skipper = SkipObject(alpha)  # container object
    It = iter(skipper)
    print(next(It), next(It), next(It))  # a c e offsets 0, 2, 4
    print('')

    for x in skipper:  # calls __iter__() automatically
        for y in skipper:  # calls __iter__() automatically
            # aa ac ae ca cc ce ea ec ee
            print(x + y, end=' ')
    print('')
