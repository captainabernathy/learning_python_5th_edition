modname = 'string'
# NOTE: the exec() function executes its arguments as python code
exec('import ' + modname)  # has the same effect as import string

if __name__ == '__main__':
    print('code snippets from page 786.\n')
    print(dir(modname))
