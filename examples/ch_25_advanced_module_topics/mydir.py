# usage: python3 mydir.py

'''module lists the namespaces of other modules'''
from __future__ import print_function  # for 2.X compatibility

seplen = 60
sepchr = '-'


# takes the module object passed to modules and prints a formattted listing of
# the module's namespace sorted by name... verbose represents a boolean
# parameter that, when True, adds additional formatting to the module's listing
def listing(module, verbose=True):
    sepline = sepchr * seplen
    if verbose:
        print(sepline)
        print('name:', module.__name__)  # module's name
        print('file:', module.__file__)  # /path/to/module.py
        print(sepline)

    count = 0
    # loop over sorted attributes in module's dictionary
    for attr in sorted(module.__dict__):
        print('%02d) %s' % (count + 1, attr), end=' ')
        if attr.startswith('__'):
            print('<built-in name>')  # skip builtins
        else:
            # output module's attributes
            print(getattr(module, attr))  # same as .__dict__[attr]
        count += 1

    if verbose:
        print(sepline)
        print(module.__name__, 'has %d names' % count)  # summary
        print(sepline)


if __name__ == '__main__':
    print('code snippets from pages 784-785\n')

    # self test...
    import mydir  # import this module
    listing(mydir)  # list its contents
