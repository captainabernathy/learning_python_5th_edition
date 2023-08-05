# usage: python3 generalized_set_functions.py

from inter2 import intersect
from inter2 import union


def tester(func, items, trace=True):
    for i in range(len(items)):
        items = items[1:] + items[:1]
        if trace:
            print(items)
        print(sorted(func(*items)))


if __name__ == '__main__':
    print('code snippets from pages 566-567\n')

    s1, s2, s3 = "SPAM", "SCAM", "SLAM"
    print(intersect(s1, s2))  # ['S','A','M']
    print(union(s1, s2))  # ['S,'P','A','M','C']
    print('')

    print(intersect([1, 2, 3], (1, 4)))  # [1]... mixed types
    print(intersect(s1, s2, s3))  # ['S,','A','M']
    print(union(s1, s2, s3))  # ['S','P','A','M','C','L']
    print('')

    tester(intersect, ('a', 'abcdefg', 'abdst', 'albmcnd'))  # ['a']
    print('')

    # ['a','b','c','d','e','f','g','l','m','n','s','t']
    tester(union, ('a', 'abcdefg', 'abdst', 'albmcnd'), False)
    print('')

    # ['a','b']
    tester(intersect, ('ba', 'abcdefg', 'abdst', 'albmcnd'), False)
    print('')

    print(intersect([1, 2, 1, 3], (1, 1, 4)))  # [1]
    print(union([1, 2, 1, 3], (1, 1, 4)))  # [1,2,3,4]
    print('')
 
    tester(intersect, ('ababa', 'abcdefga', 'aaaab'), False)  # ['a','b']
