# usage: python3 alls_importer_02.py

import alls  # import all names from the alls module

if __name__ == '__main__':
    print('code snippets from page 772.\n')

    # directly access names from the alls module
    print(alls.a, alls.b, alls._c, alls._d)  # 1 2 3 4
