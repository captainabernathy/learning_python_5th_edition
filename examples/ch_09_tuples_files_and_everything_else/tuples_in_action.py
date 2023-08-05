# usage: python3 tuples_in_action.py

if __name__ == '__main__':
    print('code snippets from pages 285-286\n')

    # NOTE: (stuff,) creates a tuple... comman is necessary
    
    # Tuple operations
    print((1, 2) + (3, 4))  # (1,2,3,4)... concatenation
    print((1, 2) * 4)  # (1,2,1,2,1,2,1,2)... repetition
    print('')

    T = (1, 2, 3, 4)
    print(T)  # (1,2,3,4)
    print(T[0], T[1:3])  # 1, (2,3)
    print('')

    x = (40)  # an integer
    y = (40,)  # trailing comma makes it a tuple
    print(x)  # 40
    print(y)  # (40,)... a single item tuple
