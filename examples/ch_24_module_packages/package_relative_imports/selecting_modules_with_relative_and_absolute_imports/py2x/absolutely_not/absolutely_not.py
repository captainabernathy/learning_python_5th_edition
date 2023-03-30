# NOTE: lookups for dotted imports (from . import x, from .x import y) are
# relative-only in both python 2.X and 3.X while...
# lookups for non-dotted imports (import x, from x import y) are absolute-only
# in python 3.X, but are first relative, then absolute in python 2.X
import pkg.spam  # spam loads a string module that's relative to pkg


if __name__ == '__main__':
    print 'code snippets from page 751\n'
