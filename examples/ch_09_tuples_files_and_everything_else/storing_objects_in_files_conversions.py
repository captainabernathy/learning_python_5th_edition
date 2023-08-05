# usage: python3 storing_objects_in_files_conversions.py

if __name__ == '__main__':
    print('code snippets from pages 297-298\n')

    X, Y, Z = 43, 44, 45
    S = 'Spam'
    D = {'a': 1, 'b': 2}
    L = [1, 2, 3]

    # open/create file for writing
    F = open('datafile.txt', 'w')
    F.write(S + '\n')  # terminate lines with \n
    F.write('%s,%s,%s\n' % (X, Y, Z))  # convert numbers to strings
    F.write(str(L) + '$' + str(D) + '\n')  # convert and separate with '$'
    F.close()  # flush output buffer

    chars = open('datafile.txt').read()  # raw string display
    print(chars)

    F = open('datafile.txt')  # open file for reading
    line = F.readline()
    print(line)  # spam

    # NOTE: the rstrip() method removes the end of line character
    line = line.rstrip()
    print(line)  # Spam

    line = F.readline()
    print(line)  # 43,44,45

    # NOTE: a string's split() method converts a string to a list whose
    # elements are separated according to the delimiter provided
    parts = line.split(',')
    print(parts)  # ['43','44','45\n']
    numbers = [int(P) for P in parts]
    print(numbers)  # [43,44,45]

    line = F.readline()
    F.close()
    print(line)  # [1,2,3]${'a':1,'b':2}
    parts = line.split('$')
    print(parts)  # ['[1,2,3]',"{'a':1,'b':2}\n"]

    # NOTE: the eval() function treats a string as a piece of executable code
    objects = [eval(P) for P in parts]
    print(objects)  # [[1,2,3],{'a':1,'b':2}]
