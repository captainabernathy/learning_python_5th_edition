# usage: python3 alls_importer_01.py

# import all names defined in the alls module directly
from alls import a
from alls import b
from alls import _c
from alls import _d

if __name__ == '__main__':
    print('code snippets from page 772.\n')

    print(a, b, _c, _d)  # 1 2 3 4
