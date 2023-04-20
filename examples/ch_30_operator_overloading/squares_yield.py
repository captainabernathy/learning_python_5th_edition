# class that produces an iterable object that yields a sequence of squares
class Squares:
    # __iter__() + yield generator
    # __next__() is automatically implied
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    # coding generator as __iter__() cuts out the middleman, but...
    # iteration triggers __iter__(), which returns a new generator with
    # __next__()
    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2
