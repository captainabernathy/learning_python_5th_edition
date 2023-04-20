# class that provides a generator function that yields a sequence of squares
class Squares:
    # manual generator function calls...
    # __next__ is automatic/implied
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    # code calls to make a generator, which returns itself for __iter__()
    def gen(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2
