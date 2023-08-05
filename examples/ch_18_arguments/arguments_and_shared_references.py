# usage: python3 arguments_and_shared_references.py

def changer(a, b):
    # since a does not receive a mutable type, this change is local to
    # this function
    a = 2  # updates local copy of a
    # since b receives a mutable type, this update changes b in place
    b[0] = a * 'spam'


if __name__ == '__main__':
    print('code snippets from pages 544-545\n')

    X = 1
    L = [1, 2]
    D = {'a': 1}
    
    print(X)  # 1
    print(L)  # [1,2]
    print(D)  # {'a':1}
    print('')
    
    changer(X, L)
    
    print(X)  # 1... unchanged
    print(L)  # '['spamspam',2]'... changed
    print('')

    changer(X, D)
    print(X)  # 1... unchanged
    print(D)  # {'a':1, 0:'spamspam'}... changed
