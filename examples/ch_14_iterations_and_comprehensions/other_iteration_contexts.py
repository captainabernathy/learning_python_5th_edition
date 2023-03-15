import functools
import operator


# function that prints each of its arguments separated by a '&'
def f(a, b, c, d):
    print(a, b, c, d, sep='&')


if __name__ == '__main__':
    print('code snippets from pages 446-450\n')
    # convert each line in a file to uppercase
    for line in open('script2.py'):  # file iterators
        print(line.upper(), end='')
    print('')

    # same as ^^^ with a list comprehension
    uppers = [line.upper() for line in open('script2.py')]
    print(uppers)
    print('')

    # map is itself an iterable in 3.X
    # NOTE: the map() built-in takes a function and an iterable and applies the
    # function to each item in the iterable
    print(list(map(str.upper, open('script2.py'))))
    print('')

    # NOTE: the sorted() built-in takes an iterable object and returns a new
    # sorted list of elements contained in the object it received
    print(sorted(open('script2.py')))
    print('')

    # make a list of tuples of the lines in the file paired with each other
    print(list(zip(open('script2.py'), open('script2.py'))))
    print('')

    # make a list that contains an enumeration of the lines in a file
    print(list(enumerate(open('script2.py'))))
    print('')

    # example from the book... i think it wants to print all non-empty lines
    # in a file, but this won't work because blank lines contain the
    # the newline character, which makes them non-empty
    # print(list(filter(bool, open('script2.py'))))  # nonempty = True

    # print all non-empty elements in a list...
    print(list(filter(bool, ['hello', '', 'world'])))
    print('')

    # NOTE: the functools module's reduce() function returns the aggregate
    # result of successively applying the function it receives to each element
    # of the iterable it receives

    # concatenate each line in a file and retrun the result as a single string
    print(functools.reduce(operator.add, open('script2.py')))
    print('')

    # make a list whose elements contain the lines in a file
    print(list(open('script2.py')))
    print('')

    # make a tuple whose elements contain the lines in a file
    print(tuple(open('script2.py')))
    print('')

    # make a string joins every line in a file to '&&'
    print('&&'.join(open('script2.py')))
    print('')

    # NOTE: an attempt to perform a sequence assign with too few variables
    # results in an area
    a, b, c, d = open('script2.py')  # sequence assignment
    print(a, d)
    print('')

    # assign the first line in a file to the string a and the rest to the
    # list b
    a, *b = open('script2.py')
    print(a, b)  # a is a string, b is a list of string
    print('')

    print('y = 2\n' in open('script2.py'))  # False membership test
    print('x = 2\n' in open('script2.py'))  # True membership test
    print('')

    L = [11, 22, 33, 44]
    print(L)  # [11,22,33,44]
    
    # NOTE: a slice assignment will grow the number of elements in a list if
    # the number of elements being assigned to the slice is greater than the
    # the number of elements spanned by the slice

    # replace the elements at the indicies 1 and 2 in L with the lines of a
    # file
    L[1:3] = open('script2.py')  # [11,...,44]slice assignment
    print(L)
    print('')

    L = [11]
    print(L)  # 11
    
    # NOTE: use the extend() method to grow L by the number of lines in a file
    L.extend(open('script2.py'))  # [11,...] list.extend() method
    print(L)
    print('')

    L = [11]
    print(L)

    # NOTE: a list object's append() method does not iterate over its argument
    L.append(open('script2.py'))  # list.append() does not iterate
    print(L)  # [11, <wrapped object>]
    
    L[1:] = list(L[1])  # use the list() constructor to unpack the iterable ^^^
    print(L)  # [11,...]
    print('')

    # NOTE: the set() constructor accepts an iterables
    # make a set whose elements contain the unique lines in a file
    print(set(open('script2.py')))
    print('')

    # set comprehension
    print({line for line in open('script2.py')})  # same as ^^^
    print('')

    # dictionary comprehension whose keys are the line numbers in a file
    print({ix+1: line for ix, line in enumerate(open('script2.py'))})
    print('')

    # set comprehension of the lines in a file that start with 'p'
    print({line for line in open('script2.py') if line[0] == 'p'})
    print('')

    # dictionary comprehension whose keys are the line numbers in a file that
    # begin with 'p'
    print({ix+1: line for (ix, line) in enumerate(open('script2.py'))
           if line[0] == 'p'})
    print('')

    # NOTE: a generator expression follows iterable syntax but itself is also
    # iterable
    print(list(line.upper() for line in open('script2.py')))  # generator
    print('')

    # NOTE: the sum() function computes the sum() of all of the elements in a
    # collection
    print(sum([3, 2, 4, 1, 5, 0]))  # 15

    # NOTE: the any() function returns True if any element in the iterable it
    # receives is not None and False when all elements are None
    print(any(['spam', '', 'ni']))  # True

    # NOTE: the all() function returns True if all elements in a collection are
    # not None and False when any element is None
    print(all(['spam', '', 'ni']))  # False

    # NOTE: the max() function returns the largest element in a collection
    print(max([3, 2, 5, 1, 4]))  # 5

    # NOTE: the min() function returns the smallest element in a collection
    print(min([3, 2, 5, 1, 4]))  # 1
    print('')

    # NOTE: when used on strings, the max() function returns the string that
    # begins with the largest character value, and the min() function returns
    # the string that begins with the smallest character value
    print(max(open('script2.py')))
    print(min(open('script2.py')))

    # NOTE: use * to unpack a list
    f(*[1, 2, 3, 4])  # 1&2&3&4... unpack list in call
    print('')

    f(*open('script2.py'))

    X = (1, 2)
    Y = (3, 4)
    print(X, Y)  # (1,2) (3,4)
    print(list(zip(X, Y)))  # [(1,3), (2,4)]

    A, B = zip(*zip(X, Y))  # unzip a zip
    print(A, B)  # (1,2) (3,4)
