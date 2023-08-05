# usage: python3 counter_loops_range.py

if __name__ == '__main__':
    print('code snippets from pages 417-418\n')

    print(list(range(5)))  # [0,1,2,3,4]
    print(list(range(2, 5)))  # [2,3,4]
    print(list(range(0, 10, 2)))  # [0,2,4,6,8]
    print(list(range(-5, 5)))  # [-5,-4,-3,-2,-1,0,1,2,3,4]
    print(list(range(5, -5, -1)))  # [5,4,3,2,1,0,-1,-2,-3,-4]
    print('')

    # iterate over each element in a range
    for i in range(3):
        print(i, 'Pythons')
