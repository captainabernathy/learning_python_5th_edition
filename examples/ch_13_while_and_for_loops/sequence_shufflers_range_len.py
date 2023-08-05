# usage: python3 sequence_shufflers_range_len.py

if __name__ == '__main__':
    print('code snippets from pages 419-420\n')

    S = 'spam'
    print(S)  # spam
    print('')

    for i in range(len(S)):
        S = S[1:] + S[:1]
        print(S, end=' ')  # pams amsp mspa spam
    print('\n')

    for i in range(len(S)):
        X = S[i:] + S[:i]  # spam pams amsp mspa
        print(X, end=' ')
    print('\n')

    # technique ^^^ works for lists too
    L = [1, 2, 3]
    for i in range(len(L)):
        X = L[i:] + L[:i]  # [1,2,3], [2,3,1], [3,1,2]
        print(X, end=' ')
    print('')
