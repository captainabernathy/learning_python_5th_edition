# usage: python3 second.py

import first

if __name__ == '__main__':
    print('code snippets from pages 518-519\n')
    
    # access module's global variable
    print(first.X)  # 99
    
    first.X = 88  # update module's global X variable

    print(first.X)  # 88

    # update module's global X variable via function
    first.setX(77)

    print(first.X)  # 77
