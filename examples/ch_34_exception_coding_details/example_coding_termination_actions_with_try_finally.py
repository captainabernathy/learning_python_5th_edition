# usage: python3 example_coding_termination_actions_with_try_finally.py

class MyError(Exception):
    pass


def stuff(file):
    raise MyError()


if __name__ == '__main__':
    print('code snippets from pages 1140\n')

    file = open('data.txt', 'w')  # open a file for writing

    try:
        stuff(file)  # raises MyError
    finally:
        file.close()  # always close file to flush output buffer

    print('not reached')
