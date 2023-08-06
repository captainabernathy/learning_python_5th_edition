# usage: python3 text_file_basics.py

if __name__ == '__main__':
    print('code snippets from page 1237\n')

    f = open('temp', 'w')  # open file temp for writing
    sz = f.write('abc\n')  # write to line to temp
    f.close()  # manually close file

    f = open('temp')  # NOTE: default mode is 'r'
    text = f.read()  # read the file into text

    # abc
    # (empty line)
    print(text)
