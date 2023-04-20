# NOTE: before falling back to __getitem__() python will try __iter__() first
# class that implements the iteration protocol to generate a series of squares
class Squares:
    def __init__(self, start, stop):
        self.value = start - 1  # an internal counter
        self.stop = stop  # value to count up to

    def __iter__(self):
        return self  # get an iterator object on iter()

    def __next__(self):
        '''
        returns a square on each iteration...
        also called by next() built-in
        '''
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2
