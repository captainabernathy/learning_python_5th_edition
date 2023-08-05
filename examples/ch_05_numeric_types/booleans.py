# usage: python3 booleans.py

if __name__ == '__main__':
    print('code snippets from page 177\n')

    print(type(True))  # <class 'bool'>
    print(isinstance(True, int))  # True
    print(True == 1)  # True... not wrong, but flake8 doesn't like
    print(True is 1)  # False.. not wrong, but flake8 doesn't like
    print(True or False)  # True
    print(True + 4)  # 5
