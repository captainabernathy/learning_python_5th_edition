# usage: python3 main.py

# NOTE:  when you isolate all but the main files used only by the program in a
# subdirectory, intrapackage imports still work in 2.X and 3.X... as such, you
# can use the top directory as a standalone program, and the nested directory
# still serves as a package for use from other programs
import sub.spam


if __name__ == '__main__':
    print('code snippets from page 756\n')
