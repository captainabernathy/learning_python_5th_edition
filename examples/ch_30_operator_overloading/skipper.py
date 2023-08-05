# usage: python3 skipper.py

# class defines an interable object that skips every other item on iterations
class SkipObject:
    def __init__(self, wrapped):  # save item to be used
        self.wrapped = wrapped

    # returns a new SkipIterator each call
    def __iter__(self):
        return SkipIterator(self.wrapped)


class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped  # this SkipIterator's state information
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):  # terminate iterations
            raise StopIteration
        else:
            item = self.wrapped[self.offset]  # get item at offset
            self.offset += 2  # update offest for next item to get
            return item


if __name__ == '__main__':
    print('code snippets from pages 928-930\n')

    alpha = 'abcdef'
    skipper = SkipObject(alpha)  # container object
    It = iter(skipper)  # take an iterator to it
    print(next(It), next(It), next(It))  # a c e... offsets 0, 2, 4
    print('')

    for x in skipper:  # for calls __iter__() automatically
        for y in skipper:  # Nested for-s call __iter__() again
            # NOTE: each iterator has its own state, offset
            print(x + y, end=' ')  # aa ac ae ca cc ce ea ec ee
    print('')

    # classes vs slices... similar to ^^^, but less efficient
    S = 'abcdef'
    for x in S[::2]:  # slices produce new objects and store results in memory
        for y in S[::2]:
            print(x + y, end=' ')  # aa ac ae ca cc ce ea ec ee
    print('')

    S = 'abcdef'
    S = S[::2]
    print(S)  # ace
    for x in S:  # more similar to iterator version
        for y in S:  # same object, new iterators
            print(x + y, end=' ')  # aa ac ae ca cc ce ea ec ee
