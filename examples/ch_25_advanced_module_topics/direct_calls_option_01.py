# usage: python3 direct_calls_option_01.py

modname = 'string'
# NOTE: the built-in __import__() function loads a module with the name of its
# argument and returns a top-level module object... it is recommended to run
# importlib.import_module() over __import__()
string = __import__(modname)  # built-in __import__() function

if __name__ == "__main__":
    print('code snippets from page 787.\n')

    print(string)  # <module 'string' from '/path/to/string.py'>
