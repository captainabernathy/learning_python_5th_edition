if __name__ == '__main__':
    print('code snippets from pages 101-103\n')
    # assignment
    S = 'Spam'

    print(S)  # Spam

    # len() function
    print(len(S))  # 4

    # first item in S
    print(S[0])  # S

    # second item in S
    print(S[1])  # p

    # last item in S
    print(S[-1])  # m

    # second to last item in S
    print(S[-2])  # a

    # also the last item in S
    print(S[len(S) - 1])  # S[3]... m

    # slice of S containing from offset 1 up to but not includeing offset 3
    print(S[1:3])  # pa

    # everything but the first item in S
    print(S[1:])  # pam

    # everything but the last item in S
    print(S[0:3])  # Spa

    # alternatively...
    print(S[:3])  # Spa

    # easiest alternative... everything but the last item in S
    print(S[:-1])  # Spa

    # top level copy
    T = S[:]
    print(T)  # Spam

    # string concatenation
    print(S + 'xyz')  # Spamxyz

    # string repetition
    print(S * 8)  # SpamSpam...Spam
