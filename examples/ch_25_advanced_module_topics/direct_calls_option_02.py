import importlib
modname = 'string'
# NOTE: importlib.import_module() loads a module with the name of its argument
# and returns the specified module object... it is recommended to use
# importlib.import_module() over __import__()
string = importlib.import_module(modname)

if __name__ == "__main__":
    print('code snippets from page 787.\n')
    print(string)  # <module 'string' from '/path/to/string.py'>
