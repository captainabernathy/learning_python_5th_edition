# NOTE: runs this with python3

# NOTE: in python >= 3.2 byte code files are saved in a __pycache__
# subdirectory
import script0  # creates a __pycache__ dirctory in this directory

if __name__ == '__main__':
    print('code snippets from pages 699-700\n')
    # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
    #  '__loader__', '__name__', '__package__', '__spec__', 'script0']
    print(dir())
