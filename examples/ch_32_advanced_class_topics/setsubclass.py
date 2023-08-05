# usage: python3 setsubclass.py

# program implements a class that extends python's list class so that it
# provides "set-like" features and demonstrates its usage

# class extends python's list class to prvoide "set-like" features
class Set(list):  # subclass list to implement a set
    # constructor... provides a an empty Set by default or uses the list passed
    # to value to initialize this Set
    def __init__(self, value=[]):
        list.__init__([])
        self.concat(value)  # no need to manage data directly

    # adds values from the iterable sequence passed to value that are not
    # present in Set to it
    def concat(self, value):
        # loop over each value
        for x in value:
            # only append values that do not exist in this Set to it
            if x not in self:
                self.append(x)

    # returns a new Set that contains the set intersection of this Set and the
    # iterable sequence passed to other
    def intersect(self, other):
        res = []  # start empty
        # loop over this Set's data
        for x in self:
            # only append items to the result if they also exist in other
            if x in other:
                res.append(x)
        return Set(res)  # return a new Set containing the results

    # retuns a new Set that contains the set union of this Set and the iterable
    # sequence passed to other
    def union(self, other):
        # start with a copy of this Set, since it must be part of the union
        res = Set(self)
        # concatenate elements from other that do not yet exist in the result
        # to it
        res.concat(other)
        return res  # return result

    # returns a new Set that contains the set intersection of this Set and the
    # iterable sequence passed to other
    def __and__(self, other):
        return self.intersect(other)

    # retuns a new Set that contains the set union of this Set and the iterable
    # sequence passed to other
    def __or__(self, other):
        return self.union(other)

    # returns the number of elements are contained in this Set's data
    def __repr__(self):
        return 'Set:' + list.__repr__(self)


if __name__ == '__main__':
    print('code snippets from pages 1016-1017\n')

    # build some sets
    x = Set([1, 3, 5, 7])
    y = Set([2, 1, 4, 5, 6])
    print(x)  # Set:[1,3,5,7]... uses overloaded __repr__()
    print(len(x))  # 4... inherits len() from list
    print(y)  # Set:[2,1,4,5,6]... uses overloaded __repr__()
    print('')

    print(x.intersect(y))  # Set:[1,5]
    print(y.union(x))  # Set:[2,1,4,5,6,3,7]
    print(x & y)  # Set:[1,5]
    print(x | y)  # Set:[1,3,5,7,2,4,6]
    print('')

    x.reverse()  # reverse() inherited from list
    print(x)  # Set:[7,6,3,1]
