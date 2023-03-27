import mod2  # gain access to names in mod2

X = 1  # global to this module

if __name__ == '__main__':
    print(X, end=' ')  # 1... my global X
    print(mod2.X, end=' ')  # 2... mod2's X
    print(mod2.mod3.X)  # 3... nested mod3's X
