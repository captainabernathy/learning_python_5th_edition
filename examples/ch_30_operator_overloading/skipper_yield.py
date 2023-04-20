# class defines an iterable object that yields every other item in a
# collection
class SkipObject:
    def __init__(self, wrapped):  # instance scope retained normally
        self.wrapped = wrapped  # local scope state saved automatically

    def __iter__(self):
        offset = 0
        while offset < len(self.wrapped):
            item = self.wrapped[offset]
            offset += 2
            yield item
