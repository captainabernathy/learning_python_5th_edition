# usage: python3 nonexhaustive_traversals_range_vs_slices.py

if __name__ == '__main__':
    print('code snippets from pages 420-421\n')

    S = 'abcdefghijk'
    print(S)  # abcdefghijk
    # indices of every other element in S
    print(list(range(0, len(S), 2)))  # [0,2,4,6,8,10]
    print('')

    # iterate over S by steps of 2
    for i in range(0, len(S), 2):
        print(S[i], end=' ')  # a c e g i k
    print('\n')

    # similarly...
    for c in S[::2]:
        print(c, end=' ')  # a c e g i k
    print('')
