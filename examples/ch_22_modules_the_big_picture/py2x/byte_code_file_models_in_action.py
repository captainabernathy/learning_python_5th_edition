# usage: python2 byte_code_file_models_in_action.py

# NOTE: prior to python 3.2, byte code files show up alongside their source
# files after being created by import operations
import script0  # creates a script0.pyc in this directory

if __name__ == '__main__':
    print('code snippets from pages 699-700\n')

    # ['__builtins__','__doc__','__name__','__package__','script0']
    print(dir())
