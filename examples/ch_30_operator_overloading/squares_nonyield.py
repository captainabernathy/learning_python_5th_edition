# class that produces an iterable object that produces a sequence of squares
class Squares:
    # non-yield generator
    # multi-scans: extra object
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        # extra object stores iterator state
        return SquaresIter(self.start, self.stop)


# helper class that provides a __next__() method to complement Square's
# __iter__() method
class SquaresIter:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2
