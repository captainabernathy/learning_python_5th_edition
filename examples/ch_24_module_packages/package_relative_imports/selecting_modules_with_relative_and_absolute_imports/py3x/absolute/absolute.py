# usage: python3 absolute.py

# NOTE: lookups for dotted imports (from . import x, from .x import y) are
# relative-only in both python 2.X and 3.X while...
# lookups for non-dotted imports (import x, from x import y) are absolute-only
# in python 3.X, but are first relative, then absolute in python 2.X
import pkg.spam  # spam loads python's string module via an absolute import


if __name__ == '__main__':
    print('code snippets from page 751\n')
