# usage: python3 mod2.py

import mod3  # gain access to names in mod3

X = 2  # global to this file

if __name__ == '__main__':
    print('code snippets from page 723\n')

    print(X, end=' ')  # 2... my global X
    print(mod3.X)  # 3... mod3's X
