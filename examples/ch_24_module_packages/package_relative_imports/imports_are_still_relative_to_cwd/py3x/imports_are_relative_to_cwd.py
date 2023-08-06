# usage: python3 imports_are_relative_to_cwd.py

import pkg.spam  # module's lookup will load string module from this directory


if __name__ == '__main__':
    print('code snippets from page 750\n')
