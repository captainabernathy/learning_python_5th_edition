# function returns a list whose elements contain all of the permutations of
# the elements in seq
def permute1(seq):
    if not seq:
        return [seq]  # empty sequence
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]  # delete current node
            for x in permute1(rest):  # permute the others
                res.append(seq[i:i+1] + x)  # add node at front (build up res)
        return res


# NOTE: generator functions retain their local state while active
# generator function that successively yields each of the permutations of the
# elements in seq
def permute2(seq):
    if not seq:
        yield seq  # empty sequence
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]  # remove current element from sequence
            for x in permute2(rest):  # permute remaining elements
                yield seq[i:i+1] + x  # form a result
