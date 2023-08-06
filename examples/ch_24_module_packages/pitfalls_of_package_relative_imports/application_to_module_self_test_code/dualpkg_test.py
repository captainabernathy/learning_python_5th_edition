# usage: python3 dualpkg_test.py

import dualpkg.m2  # no need to update PYTHONPATH

if __name__ == '__main__':
    print('code snippets from pages 757-758\n')

    dualpkg.m2.somefunc()  # calls m1.somefunc()
