# usage: python3 global_statement.py

# X, y, and z are globally defined integers
X = 88
y, z = 1, 2


# function access global variable X and changes its value
def func():
    global X
    X = 99  # change global X


# function creates a global variable x and assigns a value to it
def all_global():
    global x  # creates x in global scope
    x = y + z  # access y and z via scope lookup rules


if __name__ == '__main__':
    print('code snippets from pages 515-516\n')

    print(X)  # 88
    func()  # changes X
    print(X)  # 99
    all_global()  # creates variable x in global scope
    print(x)  # 3
