# usage: python3 import_and_from_are_assignments_01.py

# NOTE: an import statement assigns an entire module object to a single name
import small

# NOTE: a from statement assigns one or more names to objects of the same name
# in another module
from small import x
from small import y


if __name__ == '__main__':
    print('code snippets from pages 715-716\n')

    print(x)  # 1... small's x
    print(y)  # [1,2]... small's y
    print('')

    # NOTE: small's x is not a shared mutable object, but small's y is, so
    # changes to x in this file don't affect small's x, but changes to y in
    # this file do affect small's y
    x = 42  # changes local x only
    y[0] = 42  # changes shared mutable in place
    print(x)  # 42
    print(y)  # [42,2]
    print('')

    print(small.x)  # 1... unchanged
    print(small.y)  # [42, 2]... changed
