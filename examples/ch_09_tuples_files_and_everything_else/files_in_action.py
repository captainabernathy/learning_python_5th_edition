if __name__ == '__main__':
    print('code snippets from pages 294-295\n')

    # NOTE: open() returns a file object
    myfile = open('myfile.txt', 'w')  # open/create text file for writing
    # use the write() method to write text to a file
    myfile.write('hello text file\n')
    myfile.write('goodbye text file\n')
    myfile.close()  # flush output buffers

    myfile = open('myfile.txt')  # open text file for reading ('r' default)
    print(myfile.readline(), end='')  # read a line
    print(myfile.readline())

    print(open('myfile.txt').read())  # read all at once into a string

    # iterate over lines in a file
    for line in open('myfile.txt'):
        print(line, end='')
