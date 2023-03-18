# function outputs its arguments... calls must receive 3 arguments
def f1(a, b, c):
    print(a, b, c)


# function outputs its arguments... calls only reqire a single argument
def f2(a, b=2, c=3):  # a required, b and c optional
    print(a, b, c)


# fuction outputs its arguments... calls require 2 arguments
def func(spam, eggs, toast=0, ham=0):
    print((spam, eggs, toast, ham))


if __name__ == '__main__':
    print('code snippets from pages 552-554\n')
    # pass a, b, and c by position
    f1(1, 2, 3)

    # pass a, b, and c by keyword
    f1(c=3, b=2, a=1)  # 1 2 3
    print('')

    # pass a by position, and pass b and c by keyword
    f1(1, c=3, b=2)  # 1 2 3
    print('')

    # use defaults for b and c
    f2(1)  # 1 2 3
    f2(a=1)  # 1 2 3... same as ^^^

    # pass a and by by position and use default for c
    f2(1, 4)  # 1 4 3... overrides default for b

    # pass a, b, and c by position
    f2(1, 4, 5)  # 1 4 5... overrides defaults for b and c

    # pass a by position, use default for b, and pass c by keyword
    f2(1, c=6)  # 1 2 6... uses default b and overrides default for c
    print('')

    # pass spam and eggs by position, use defaults for toast and ham
    func(1, 2)  # (1,2,0,0)

    # pass spam by position, pass ham and eggs by keyword, use default for
    # toast
    func(1, ham=1, eggs=0)  # (1,0,0,1)... overrides ham, specifies eggs
    
    # pass spam and eggs by keyword, use defaults for toast and ham
    func(spam=1, eggs=0)  # (1,0,0,0)... specifies spam and eggs
    
    # pass toast, eggs, and spam by keyword, use default for ham
    func(toast=1, eggs=2, spam=3)  # (3,2,1,0)... # specifies spam and eggs,
                                   # overrides default for toast, and uses
                                   # default for ham
 
    # pass spam, eggs, toast, and ham by position
    func(1, 2, 3, 4)  # (1,2,3,4)... overrides defaults for toast and ham
