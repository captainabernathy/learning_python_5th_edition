# generator function that yields reorderings of the elements in seq such that
# the first element in seq is successively moved to the end of the sequqnce
# for each element in seq
def scramble(seq):
    for i in range(len(seq)):  # generator function
        yield seq[i:] + seq[:i]  # yield one item per iteration
