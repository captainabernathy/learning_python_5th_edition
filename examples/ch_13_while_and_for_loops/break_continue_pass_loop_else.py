# usage: python3 break_continue_pass_loop_else.py

if __name__ == '__main__':
    print('code snippets from pages 402-407\n')

    x = 10
    while x:
        x -= 1
        if x % 2 != 0:
            continue  # jumps to the top of the closest enclosing loop
        print(x, end=' ')  # 8 6 4 2 0
    print('')

    # similarly...
    x = 10
    while x:
        x -= 1
        if x % 2 == 0:
            print(x, end=' ')  # 8 6 4 2 0
    print('')
    print('')

    while True:
        name = input('Enter name (or stop to quit): ')
        if name == 'stop':
            break  # exits the closest enclosing loop
        age = input('Enter age: ')
        print('Hello,', name, '=>', int(age) ** 2)
    print('')

    y = 7
    x = y // 2
    while x > 1:
        if y % x == 0:
            print(y, 'has factor', x)
            break
        x -= 1
    else:  # runs if and only if loop exits normally... i.e. doesn't break
        print(y, 'is prime')  # loop else
    print('')
