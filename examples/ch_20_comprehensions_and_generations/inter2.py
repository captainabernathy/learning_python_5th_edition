# function returns a list that contains the set intersection of any number of
# sequential collections
def intersect(*args):
    res = []  # start empty
    for x in args[0]:  # loop over each item in first arg
        if x in res:
            continue  # skip duplicates
        for other in args[1:]:  # loop over each item in the rest of the args
            if x not in other:  # don't add x to the results if it's not
                break           # in of the other args
        else:
            res.append(x)  # found x... append to results
    return res


# function returns a list that contains the union of any number of sequential
# collections
def union(*args):
    res = []  # start emepty
    for seq in args:  # loop over each of the sequences
        for x in seq:  # loop over each item in each sequence
            if x not in res:  # appended item to results if it isn't already
                res.append(x)  # included in the results
    return res
