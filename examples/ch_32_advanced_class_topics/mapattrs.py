'''
mapattrs.py

The mapattrs() function maps all attributes on or inherited by an instance to
the instance or class the attributes are inherited from, and returns a
dictionary that contains the results.

It assumes that dir() returns all of an instance's attributes. To simulate
inheritance, it uses either the class's MRO tuple, which gives the search order
for new-style classes (and all classes in 3.X), or a recursive traversal to
infer the DFLR order of classic classes in 2.X.

The inheritance() function  returns a tuple that contains a version-neutral
class ordering

Additionally this module provides assorted dictionary tools that use 3.X/2.7
comprehensions
'''

import pprint  # outputs lists and dictionaries nicely


def trace(X, label='', end='\n'):
    print(label + pprint.pformat(X) + end)  # print nicely


# returns a dictionary that contains all of the key-value pairs of D except
# the pairs whose keys map to the value of V
def filterdictvals(D, V):
    '''
    dict D with entries for value V removed...
    filterdictvals(dict(a=1, b=2, c=1), 1) => {'b': 2}
    '''
    return {K: V2 for (K, V2) in D.items() if V2 != V}


# returns a dictionary whose key-value pairs are mappings from the values of
# D to its keys
def invertdict(D):
    '''
    dict D with values changed to keys (grouped by values)...
    values must all be hashable to work as dict/set keys
    invertdict(dict(a=1, b=2, c=1)) => {1: ['a', 'c'], 2: ['b']}
    '''
    def keysof(V):
        return sorted(K for K in D.keys() if D[K] == V)
    return {V: keysof(V) for V in set(D.values())}


# performs a depth-first, left-to-right traversal of cls's class tree and
# returns the results in a tuple
def dflr(cls):
    '''
    class depth-first, left-to-right order of class tree at cls...
    cycles not possible... python disallows on __bases__ changes
    '''
    #  here = [cls]
    here = (cls,)
    for sup in cls.__bases__:
        here += dflr(sup)
    return here


# returns a tuple that contains instance's inheritance hierarchy
def inheritance(instance):
    '''
    inheritance order sequence: new-style (MRO) or classic (DFLR)
    '''
    if hasattr(instance.__class__, '__mro__'):
        return (instance,) + instance.__class__.__mro__
    else:
        #  return [instance] + dflr(instance.__class__)
        return (instance,) + dflr(instance.__class__)


# returns a dictionary whose keys represent instance's inherited attributes and
# whose values are represented by the objects instance has inherited the key
# from
def mapattrs(instance, withobject=False, bysource=False):
    '''
    dict with keys giving all inherited attributes of instance and values
    giving the object that each is inherited from.

    withobject: False=remove object built-in class attributes

    bysource: True=group result by objects instead of attributes...
    supports classes with slots that preclude __dict__ in instances
    '''
    attr2obj = {}  # start empty

    # get instance's inheritance tree
    inherits = inheritance(instance)

    # loop over all of instance's attributes
    for attr in dir(instance):
        # loop over instance's inheritance hierarchy
        for obj in inherits:
            # if an object that instance inherits from has a __dict__ and
            # that object's __dict__ is on of instance's attributes, map the
            # attribute to the object in the dictionary
            if hasattr(obj, '__dict__') and attr in obj.__dict__:  # see slots
                attr2obj[attr] = obj
                break

    # filter as prescribed and return results
    if not withobject:
        attr2obj = filterdictvals(attr2obj, object)
    return attr2obj if not bysource else invertdict(attr2obj)


if __name__ == '__main__':
    print('code snippets from pages 1039-1042\n')

    print('Classic classes in 2.x, new-style in 3.x')

    class A:
        attr1 = 1

    class B(A):
        attr2 = 2

    class C(A):
        attr1 = 3

    class D(B, C):
        pass

    It = D()
    print('Py=>%s' % It.attr1)
    trace(inheritance(It), 'INH\n')  # D's inheritance tree
    trace(mapattrs(It), 'ATTRS\n')  # D's attriutes... as attr=>obj

    # D's attributes grouped by the object they were inherited from
    trace(mapattrs(It, bysource=True), 'OBJS\n')  # obj=>[attrs...]
    print('')

    print('New-style classes in 2.x and 3.x')

    class A(object):
        attr1 = 1

    class B(A):
        attr2 = 2

    class C(A):
        attr1 = 3

    class D(B, C):
        pass

    It = D()
    print('Py=>%s' % It.attr1)
    trace(inheritance(It), 'INH\n')  # D's inheritance tree
    trace(mapattrs(It), 'ATTRS\n')  # D's attributes... as attr=>obj

    # D's attributes grouped by the object they were inherited from
    trace(mapattrs(It, bysource=True), 'OBJS\n')  # obj=>[attrs...]
    print('')
