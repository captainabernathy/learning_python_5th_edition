# NOTE: the first import loads and runs a file's code... subsequents imports
# don't rerun the module's code... they just fetch the already created module
# object from python's internal modules table
import simple

if __name__ == '__main__':
    print('code snippets from pages 714-715\n')
    print(simple.spam)  # 1

    simple.spam = 2
    print(simple.spam)  # 2

    import simple  # doesn't reinitialize spam
    print(simple.spam)  # 2
