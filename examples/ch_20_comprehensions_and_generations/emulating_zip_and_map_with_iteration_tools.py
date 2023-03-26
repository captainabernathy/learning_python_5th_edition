if __name__ == '__main__':
    print('code snippets from pages 640-644\n')
    S1 = 'abc'
    S2 = 'xyz123'
    print(list(zip(S1, S2)))  # [('a','x'),('b','y'),('c','z')]
    print('')

    print(list(zip([-2, -1, 0, 1, 2])))  # [(-2,),(-1,),(0,),(1,),(2,)]
    print('')

    print(list(zip([1, 2, 3], [2, 3, 4, 5])))  # [(1,2),(2,3),(3,4)]
    print('')

    print(list(map(abs, [-2, -1, 0, 1, 2])))  # [2,1,0,1,2]
    print('')

    print(list(map(pow, [1, 2, 3], [2, 3, 4, 5])))  # [1,8,81]
