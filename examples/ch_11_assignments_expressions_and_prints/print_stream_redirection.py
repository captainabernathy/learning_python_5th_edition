# usage: python3 print_stream_redirection.py

import sys

if __name__ == '__main__':
    print('code snippets from pages 376-378\n')

    # write hello world to stdout with print() function
    print('hello world')

    # write hello world to stdout by calling the write() method of sys.stdout
    sys.stdout.write('hello world\n')  # printing the hard way

    X = 1
    Y = 2
    # NOTE: str() converts its argment to a string
    sys.stdout.write(str(X) + ' ' + str(Y) + '\n')  # 1 2
    print('')

    # manual stream redirection
    # line below attaches stdout to log.txt and leaves us unable to restore it
    # sys.stdout = open('log.txt', 'a')

    # automatic stream redirection
    # save current output stream to variable... for restoring later
    temp = sys.stdout
    # now attach stdout to log.txt
    sys.stdout = open('log.txt', 'w')  # redirect prints to a file

    # write to log.txt
    print('spam')
    print(1, 2, 3)

    sys.stdout.close()  # flush output buffer to disk
    sys.stdout = temp  # restore stdout

    print('back here')  # writes to terminal
    print(open('log.txt').read())  # outputs contents of log.txt

    log = open('log.txt', 'w')  # truncate and open log.txt for writing
    # use the print() function's file keyword argument to send its output to
    # a file
    print(1, 2, 3, file=log)
    print(4, 5, 6, file=log)
    log.close()  # close log file

    print(7, 8, 9)
    print('')
    print(open('log.txt').read())  # outputs contents of log file
    print('')

    sys.stderr.write(('Bad!' * 8) + '\n')  # write to stderr
    print('Bad!' * 8, file=sys.stderr)  # same as ^^^
    print('')

    sys.stdout.write(str(X) + ' ' + str(Y) + '\n')  # 1 2 printing the hard way
    print('')
    
    # NOTE: open() returns a file object
    print(X, Y, file=open('temp1.txt', 'w'))  # redirect text to a file
    
    # manual output redirection to a file
    open('temp2', 'w').write(str(X) + ' ' + str(Y) + '\n')
    
    # read and output the contents of two previously written files
    print(open('temp1.txt', 'rb').read())
    print(open('temp2.txt', 'rb').read())
