import manynames

if __name__ == '__main__':
    print('code snippets from page 903\n')
    X = 66
    print(X)  # 66... __main__' X
    print(manynames.X)   # 11... globals become attributes after imports
    print('')

    manynames.f()  # 11... accesses manyname's X
    manynames.g()  # 22... accesses g()'s local X
    print('')

    print(manynames.C.X)  # 33... class attribute

    MyInstance = manynames.C()

    print(MyInstance.X)  # 33... hasn't changed

    MyInstance.m()  # sets MyInstance's X
    print(MyInstance.X)  # 55... MyInstance's X
