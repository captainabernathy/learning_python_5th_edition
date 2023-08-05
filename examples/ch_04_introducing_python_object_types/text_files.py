# usage: python3 text_files.py

if __name__ == '__main__':
    print('code snippets from pages 125-126\n')

    # the open() creates a file if it does not already exist
    f = open('data.txt', 'w')

    # the write() method writes a string to the file
    f.write('Hello\n')
    f.write('World\n')

    # use the close() method to close the file
    f.close()

    # open a file for reading
    f = open('data.txt')  # 'r' is the default mode

    # read entire file into a string
    text = f.read()
    f.close()
    print(text)  # output contents read

    # split() the text into a list of strings
    print(text.split())  # ['Hello', 'World']

    # output text line-by-line
    for line in open('data.txt'):
        print(line)
