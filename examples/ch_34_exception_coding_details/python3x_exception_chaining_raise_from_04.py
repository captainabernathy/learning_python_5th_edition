# usage: python3 python3x_exception_chaining_raise_from_04.py

if __name__ == '__main__':
    print('code snippets from page 1151\n')

    # implict chaining
    try:
        try:
            1 / 0
        except:
            badname
    except:
        open('nothing')
