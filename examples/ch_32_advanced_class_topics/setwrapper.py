# class provides a "set-like" interface that uses a list to manage its data
# internally. Set objects support the following operations and operators:
# union(), concat(), intersect(), __len__(), __getitem__(), __and__(),
# __or__(), __repr__(), and __iter__(), where __and__() is a synonym for
# intersect(), and __or__() is a synonym for union()
class Set:
    # constructor... provides a an empty Set by default or uses the list passed
    # to value to initialize this Set
    def __init__(self, value=[]):
        self.data = []  # start empty
        self.concat(value)  # add the unique values in value to this Set's data

    # adds values from the iterable sequence passed to value that are not
    # present in this Set's data to it
    def concat(self, value):
        # loop over each value
        for x in value:
            # only append values that do not exist in this Set's data to it
            if x not in self.data:
                self.data.append(x)

    # returns a new Set that contains the set intersection of this Set's data
    # and the iterable sequence passed to other
    def intersect(self, other):
        res = []  # start empty
        # loop over this Set's data
        for x in self.data:
            # only append items to the result if they also exist in other
            if x in other:
                res.append(x)
        return Set(res)  # return new Set that contains the result

    # retuns a new Set that contains the set union of this Set's data and the
    # iterable sequence passed to other
    def union(self, other):
        # make a copy of this Set's data, since it must be part of the union
        res = self.data[:]
        # loop of the other's data
        for x in other:
            # only append items to the result that are not yet a part of it
            if x not in res:
                res.append(x)
        return Set(res)  # return new Set that contains the result

    # returns the number of elements are contained in this Set's data
    def __len__(self):
        return len(self.data)

    # returns the element at position key from this Set's data
    def __getitem__(self, key):
        return self.data[key]
    
    # returns a new Set that contains the set intersection of this Set's data
    # and the iterable sequence passed to other
    def __and__(self, other):
        return self.intersect(other)

    # retuns a new Set that contains the set union of this Set data and the
    # iterable sequence passed to other
    def __or__(self, other):
        return self.union(other)

    # returns the string representation of this Set
    def __repr__(self):
        return 'Set:' + repr(self.data)

    # returns an iterator to this Set's data
    def __iter__(self):
        return iter(self.data)
