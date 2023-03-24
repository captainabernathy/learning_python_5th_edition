# returns a list containing the results of mapping func successively
# to each sequence contained in seqs
def mymap1(func, *seqs):
    '''map(func, seqs...) workalike with zip'''
    res = []  # start empty
    # build up results by calling func on each sequence of arguments in args
    for args in zip(*seqs):
        res.append(func(*args))
    return res


# returns a list containing the results of mapping func successively
# to each sequence contained in seqs
def mymap2(func, *seqs):
    '''map(func, seqs...) via list comprehension'''
    return [func(*args) for args in zip(*seqs)]


# generator function that yields the results of  mapping func successively to
# each sequence contained in seqs
def mymap3(func, *seqs):
    '''map(func, seqs...) via generators w/yield'''
    for args in zip(*seqs):  # loop over each sequence of arguments in seqs
        yield func(*args)  # yield the result for each call on demand


# returns a generator expression that yields the results of mapping func
# successively to each sequence contained in seqs
def mymap4(func, *seqs):
    '''map(func, seqs...) via generators (...)'''
    return (func(*args) for args in zip(*seqs))


# function that returns a list that has the same length as the shortest
# sequence in seqs and contains elements such that each element consists of a
# tuple that contains the elements at the same position for each of the
# sequences in seq
def myzip1(*seqs):
    '''zip(seqs...) workalike'''
    seqs = [list(S) for S in seqs]  # build a list of sequences
    res = []  # start empty
    # build up the results by popping the top off of each sequence until the
    # shortest sequence is empty
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res


# function that returns a list that has the same length as the longest
# sequence in seqs and contains elements such that each element consists of a
# tuple that contains the elements at the same position for each of the
# sequences in seq
# when the length of the sequences in seq are not equal, the object provided to
# pad will be used to fill in the results when the shorter sequences run out
# of elements
def mymapPad1(*seqs, pad=None):
    '''2.X map(None, seqs...) workalike'''
    seqs = [list(S) for S in seqs]  # build list of sequences
    res = []  # start emtpy
    # build up the results by popping the off of each sequence until all of
    # them are emtpy using pad in place of missing elements until the longest
    # sequence is empty
    while any(seqs):
        res.append(tuple((S.pop(0) if S else pad) for S in seqs))
    return res


# generator function that yields results that consist of a tuple that contains
# the elements at the same position for each sequence in seqs
# the maximum number of results that can be yieled from any particular call
# is the same as the number of element contained in the shortest sequence in
# seqs
def myzip2(*seqs):
    '''zip(seqs...) using generator w/yield'''
    seqs = [list(S) for S in seqs]  # build list of sequences
    # yield the result of popping the top off of each sequence on demand
    # until the shortest sequence is empty
    while all(seqs):
        yield tuple(S.pop(0) for S in seqs)


# generator function that yields results that consist of a tuple that contains
# the elements at the same position for each sequence in seqs
# the maximum number of results that can be yielded from any particular call is
# the same as the number of elements contained in the longest sequence in seqs
# when the length of the sequences in seq are not equal, the object provided to
# pad will be used to fill in the results when the shorter sequences run out
# of elements
def mymapPad2(*seqs, pad=None):
    '''2.X map(None, seqs...) using generator w/yield'''
    seqs = [list(S) for S in seqs]  # build up list of sequences
    # yield the result of popping the top off of each sequence on demand using
    # pad in place of missing elements until the longest longest sequence is
    # empty
    while any(seqs):
        yield tuple((S.pop(0) if S else pad) for S in seqs)


# function that returns a list that has the same length as the shortest
# sequence in seqs and contains elements such that each element consists of a
# tuple that contains the elements at the same position for each of the
# sequences in seq
def myzip3(*seqs):
    '''zips(seqs...) with lengths'''
    minlen = min(len(S) for S in seqs)  # find length of the shortest sequence
    # return a list that contains minlen tuples, each of which consists of
    # the elements at the same position in each sequence
    return [tuple(S[i] for S in seqs) for i in range(minlen)]


# function that returns a list that has the same length as the longest
# sequence in seqs and contains elements such that each element consists of a
# tuple that contains the elements at the same position for each of the
# sequences in seq
# when the length of the sequences in seq are not equal, the object provided to
# pad will be used to fill in the results when the shorter sequences run out
# of elements
def mymapPad3(*seqs, pad=None):
    '''2.X map(None, seqs...) using lengths'''
    maxlen = max(len(S) for S in seqs)  # find length of longest sequence
    # return a list that contains maxlen tuples, each of which consists of the
    # element at the same position in each sequene using pad in place of
    # missing elements
    return [tuple((S[i] if len(S) > i else pad) for S in seqs)
            for i in range(maxlen)]


# function that returns a generator expression that yields results that consist
# of a tuple that contains the elements at the same position for each sequence
# in seqs
# the maximum number of results that can be yieled from any particular call
# is the same as the number of element contained in the shortest sequence in
# seqs
def myzip4(*seqs):
    '''zips(seqs...) using generator w/(...)'''
    minlen = min(len(S) for S in seqs)  # find length of shortest sequence
    return (tuple(S[i] for S in seqs) for i in range(minlen))


# function that returns a generator expression that yields results that consist
# of a tuple that contains the elements at the same position for each sequence
# in seqs
# the maximum number of results that can be yielded from any particular call
# is the same as the number of elements contained in the shortest sequence in
# seqs
# when the length of the sequences in seq are not equal, the object provided to
# pad will be used to fill in the results when the shorter sequences run out
# of elements
def mymapPad4(*seqs, pad=None):
    maxlen = max(len(S) for S in seqs)  # find lenght of longest sequence
    return (tuple((S[i] if len(S) > i else pad)
                  for S in seqs) for i in range(maxlen))


if __name__ == '__main__':
    print('code snippets from pages 640-644\n')
    print(mymap1(abs, [-2, -1, 0, 1, 2]))  # [2,1,0,1,2]
    print(mymap1(pow, [1, 2, 3], [2, 3, 4, 5]))  # [1,8,81]
    print('')

    print(mymap2(abs, [-2, -1, 0, 1, 2]))  # [2,1,0,1,2]
    print(mymap2(pow, [1, 2, 3], [2, 3, 4, 5]))  # [1,8,81]
    print('')

    print(list(mymap3(abs, [-2, -1, 0, 1, 2])))  # [2,1,0,1,2]
    print(list(mymap3(pow, [1, 2, 3], [2, 3, 4, 5])))  # [1,8,81]
    print('')

    print(list(mymap4(abs, [-2, -1, 0, 1, 2])))  # [2,1,0,1,2]
    print(list(mymap4(pow, [1, 2, 3], [2, 3, 4, 5])))  # [1,8,81]
    print('')

    S1, S2 = 'abc', 'xyz123'
    print(myzip1(S1, S2))  # [('a','x'),('b','y'),('c','z')]
    # [('a','x'),('b','y'),('c','z'),(None,'1'),(None,'2'),(None,'3')]
    print(mymapPad1(S1, S2))  # default padding
    # [('a','x'),('b','y'),('c','z'),(99,'1'),(99,'2'),(99,'3')]
    print(mymapPad1(S1, S2, pad=99))  # pad with 99
    print('')

    S1, S2 = 'abc', 'xyz123'
    print(list(myzip2(S1, S2)))  # [('a','x'),('b','y'),('c','z')]
    # [('a','x'),('b','y'),('c','z'),(None,'1'),(None,'2'),(None,'3')]
    print(list(mymapPad2(S1, S2)))  # default padding
    # [('a','x'),('b','y'),('c','z'),(99,'1'),(99,'2'),(99,'3')]
    print(list(mymapPad2(S1, S2, pad=99)))  # pad with 99
    print('')

    S1, S2 = 'abc', 'xyz123'
    print(myzip3(S1, S2))  # [('a','x'),('b','y'),('c','z')]
    # [('a','x'),('b','y'),('c','z'),(None,'1'),(None,'2'),(None,'3')]
    print(mymapPad3(S1, S2))  # default padding
    # [('a','x'),('b','y'),('c','z'),(99,'1'),(99,'2'),(99,'3')]
    print(mymapPad3(S1, S2, pad=99))  # pad with 99
    print('')

    S1, S2 = 'abc', 'xyz123'
    print(list(myzip4(S1, S2)))  # [('a','x'),('b','y'),('c','z')]
    # [('a','x'),('b','y'),('c','z'),(None,'1'),(None,'2'),(None,'3')]
    print(list(mymapPad4(S1, S2)))  # default padding
    # [('a','x'),('b','y'),('c','z'),(99,'1'),(99,'2'),(99,'3')]
    print(list(mymapPad4(S1, S2, pad=99)))  # pad with 99

