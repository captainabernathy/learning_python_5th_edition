# usage: python3 runme.py

def tester():
    print("It's Christmas in Heaven...")


# NOTE: when a file is run as a top-level program, __name__ is set to __main__,
# but when a file is imported as a module, __name__ is set to the module's name
# as know by its clients (importers)
if __name__ == '__main__':
    print('code snippets from page 773\n')

    tester()  # runs when this module is not imported
