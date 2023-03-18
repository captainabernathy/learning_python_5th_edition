# function determines the set intersection for any number of iterable elements
# and returns the result
def intersect(*args):
    res = []  # start empty
    for x in args[0]:  # loop over each element in first argument
        if x in res:  # don't add x to res if it is already included in res
            continue
        for other in args[1:]:  # loop over the rest of the arguments
            if x not in other:  # if x isn't in the remaining arguments
                break           # don't add it to the results
        else:
            res.append(x)  # add x to results, since its common to the
                           # remaining arguments
    return res


# function determins the set union for any number of iterable elements and
# returns the result
def union(*args):
    res = []  # start empty
    for seq in args:  # loop of the arguments
        for x in seq:  # loop over each element of each argument
            if x not in res:  # if the current element of the current argument
                res.append(x)  # isn't already in the results, append it to
                               # the results set
    return res
