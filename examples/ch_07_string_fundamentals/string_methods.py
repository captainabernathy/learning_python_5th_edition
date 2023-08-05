# usage: python3 string_methods.py

if __name__ == '__main__':
    print('code snippets from pages 218-222\n')

    S = 'spammy'
    print(S)  # spammy
    S = S[:3] + 'xx' + S[5:]  # slice sections from S
    print(S)  # spaxxy

    S = 'spammy'
    print(S)  # spammy
    S = S.replace('mm', 'xx')  # replace() method replaces all mm with xx in S
    print(S)  # spaxxy
    print('')

    print('aa$bb$cc$dd'.replace('$', 'SPAM'))  # replace all $ with SPAM
    print('')

    S = 'xxxxSPAMxxxxSPAMxxxx'
    print(S)
    # use find() method to locate the first index of a substring in a string
    where = S.find('SPAM')
    print(S)
    print(where)  # 4
    print('')
    S = S[:where] + 'EGGS' + S[(where + 4):]
    print(S)
    print('')

    S = 'xxxxSPAMxxxxSPAMxxxx'
    print(S)
    # replace() with 2 arguments replaces all instances of the first argument
    # with the second argument in a string and returns the result
    S = S.replace('SPAM', 'EGGS')  # replace SPAM with EGGS
    print(S)
    print('')

    S = 'xxxxSPAMxxxxSPAMxxxx'
    print(S)
    # replace() with 3 arguments replaces a specified number of instances of
    # the first argument with the second argument in a string and returns the
    # result
    # replace first instance of SPAM with EGGS
    S = S.replace('SPAM', 'EGGS', 1)
    print(S)
    print('')

    S = 'spammy'
    print(S)  # spammy
    L = list(S)  # convert string to list
    print(L)  # ['s','p','a','m','m','y']

    L[3] = 'x'  # replace elements in L
    L[4] = 'x'
    print(L)  # ['s','p','a','x','x','y']

    # NOTE: the join() method joins the elements of a list into a string
    # delimited by the string that it's called on

    # join each of the elements in L in to a string with no delimiter
    S = ''.join(L)  # join() method on '' returns a string from a list
    print(S)  # spaxxy

    # join each element in the list into a string delimited by SPAM
    print('SPAM'.join(['eggs', 'sausage', 'ham', 'toast']))
    print('')

    # parsing text
    line = 'aaa bbb ccc'
    col1 = line[0:3]
    col3 = line[8:]
    print(line)  # aaa bbb ccc
    print(col1)  # aaa
    print(col3)  # ccc

    # NOTE: the split() method splits a string into a list of substrings
    # delimited by its input
    cols = line.split()
    print(cols)  # ['aaa', 'bbb', 'ccc']
    print('')

    line = 'bob,hacker,40'
    print(line)  # bob,hacker,40
    print(line.split(','))  # ['bob', 'hacker', '40']
    print('')

    line = "i'mSPAMaSPAMlumberjack"
    print(line.split("SPAM"))  # ["i'm", 'a', 'lumberjack']
    print('')

    # other common string methods
    line = "The knights who say Ni!\n"
    print(line)
    print(line.rstrip())  # use rstrip() to remove whitespace characters at end
    print(line.upper())  # use upper() convert to a string to uppercase
    # isalpha() tests if all characters in a string are letters of the alphabet
    print(line.isalpha())  # False
    # endswith() tests if a string ends with its input
    print(line.endswith('Ni!\n'))  # True
    # startswith() tests if a string starts with its input
    print(line.startswith('The'))  # True
    print('')

    # similarly
    print(line.find('Ni') != -1)  # True... search for Ni in line
    print('Ni' in line)  # True

    sub = 'Ni!\n'
    print(line.endswith(sub))  # True... test if line ends witn 'Ni!\n'
    # test if the string returned from the length of 'Ni!\n' to the end of line
    # is the same as 'Ni!\n'
    print(line[-len(sub):] == sub)  # True
