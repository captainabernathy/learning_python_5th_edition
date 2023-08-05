# usage: python3 generating_scrambled_sequences.py

# returns a list that contains reorderings of the elements in seq such that
# the first element in seq is successively moved to the end of the sequqnce
# for each element in seq
def scramble1(seq):
    res = []
    for i in range(len(seq)):
        res.append(seq[i:] + seq[:i])
    return res


# returns a list that contains reorderings of the elements in seq such that
# the first element in seq is successively moved to the end of the sequqnce
# for each element in seq
def scramble2(seq):
    return [seq[i:] + seq[:i] for i in range(len(seq))]


# generator function that yields reorderings of the elements in seq such that
# the first element in seq is successively moved to the end of the sequqnce
# for each element in seq
def scramble3(seq):
    for i in range(len(seq)):
        seq = seq[i:] + seq[:i]
        yield seq


# generator function that yields reorderings of the elements in seq such that
# the first element in seq is successively moved to the end of the sequqnce
# for each element in seq
def scramble4(seq):
    for i in range(len(seq)):
        yield seq[i:] + seq[:i]


if __name__ == '__main__':
    print('code snippets from pages 632-634\n')

    L, S = [1, 2, 3], 'spam'
    print(L)
    print(S)
    print('')

    for i in range(len(S)):
        S = S[1:] + S[:1]
        print(S, end=' ')  # pams amsp mspa spam
    print('\n')

    for i in range(len(S)):
        X = S[i:] + S[:i]
        print(X, end=' ')  # spam pams amsp mspa
    print('\n')

    print(scramble1('spam'))  # ['spam','pams','amsp', 'mspa']
    print('')

    print(scramble2('spam'))  # ['spam','pams','amsp','mspa']
    print('')

    for x in scramble2((1, 2, 3)):
        print(x, end=' ')  # [(1,2,3),(2,3,1),(3,1,2)]
    print('\n')

    print(list(scramble3('spam')))  # ['spam','pams','amsp','mspa']
    print('')
    print(list(scramble4('spam')))  # ['spam','pams','amsp','mspa']
    print('')
    print(list(scramble4((1, 2, 3))))  # [(1,2,3),(2,3,1),(3,1,2)]
    print('')

    for x in scramble4((1, 2, 3)):
        print(x, end=' ')  # [(1,2,3),(2,3,1),(3,1,2)]
    print('\n')

    print(S)  # spam
    print('')

    # generator expression that yields reorderings of the elements in S such
    # that the first element in S is successively moved to the end for each
    # element in S
    G = (S[i:] + S[:i] for i in range(len(S)))
    print(list(G))  # ['spam','pams','amsp','mspa']
    print('')

    # generalized generator expression that yields reorderings of the elements
    # of an iterable sequence such that the first element in the sequence is
    # successively moved to the end of the sequence for each element in the
    # sequence
    F = (lambda seq: (seq[i:] + seq[:i] for i in range(len(seq))))
    print(list(F(S)))
    print('')

    print(list(F((1, 2, 3))))  # [(1,2,3),(2,3,1),(3,1,2)]
    
