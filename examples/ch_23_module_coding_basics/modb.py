# usage: python3 modb.py

import moda  # gain access to names in moda

X = 11  # global to this file only

moda.f()  # sets moda.X... not this file's X

if __name__ == '__main__':
    print('code snippets from page 722\n')

    print(X, moda.X)  # 11, 99
