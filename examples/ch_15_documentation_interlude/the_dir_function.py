# returns a list that contains the named elements of the object passed to it
def dir1(x):
    return [a for a in dir(x) if not a.startswith('__')]


if __name__ == '__main__':
    print('code snippets from pages 462-464\n')
    import sys

    # NOTE: the dir() function returns a list of all of the attributes
    # available within the object passed to it... or a list of the variables
    # within the caller's scope when called with no arguments
    print(dir(sys))  # available attributes within the sys module
    print('')

    # number of attributes attributes within the sys module
    print(len(dir(sys)))
    print('')

    # print named attributes within the sys module
    print(len([x for x in dir(sys) if not x.startswith('__')]))
    print('')

    # pass dir an empty built-in to find out what attributes python provides it
    print(dir([]))  # list attributes
    print('')

    print(dir(''))  # string attributes
    print('')

    # NOTE: named methods don't start with __
    # total number of list attributes vs named list attributes
    print(len(dir([])), len([x for x in dir([]) if not x.startswith('__')]))
    # total number of string attributes vs named string attributes
    print(len(dir('')), len([x for x in dir('') if not x.startswith('__')]))
    print('')

    # named attributes of a list
    print([a for a in dir(list) if not a.startswith('__')])
    # named dict attributes
    print([a for a in dir(dict) if not a.startswith('__')])
    print('')

    print(dir1(tuple))  # named attributes of tuple
    print('')

    print(dir(str) == dir(''))  # True... same result for type name and literal
    print(dir(list) == dir([]))  # True
