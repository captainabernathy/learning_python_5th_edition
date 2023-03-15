# returns a list that contains the intersection of the elements found within
# any two iterable types it receives
def intersect(seq1, seq2):
    res = []  # start with empty list
    for x in seq1:  # scan seq1
        if x in seq2:  # search seq 2
            res.append(x)  # append to list if found
    return res


if __name__ == '__main__':
    s1 = 'SPAM'
    s2 = 'SCAM'
    print(intersect(s1, s2))  # ['S','A','M']

    # as a list comprehension
    print([x for x in s1 if x in s2])  # ['S','A','M']

    # works with any iterable type.. returns list
    # intersection of a list and a tuple
    x = intersect([1, 2, 3], (1, 4))
    print(x)  # [1]
