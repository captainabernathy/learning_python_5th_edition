if __name__ == '__main__':
    # list comprehension
    print([x * x for x in range(10) if not x % 2])  # [0,4,16,36,64]

    # NOTE: set comprehensions are enclosed in { }
    # set comprehension
    print({x * x for x in range(10) if not x % 2})  # {0,4,16,36,64}

    # NOTE: dictionary comprehensions are enclosed in { } and have
    # { key: value expression for stuff} syntax
    # dictionary comprehension
    
    # {0:0,2:4,4:16,6:36,8:64}
    print({x: x * x for x in range(10) if not x % 2})
    print('')

    # lists keep duplicates
    print([x + y for x in [1, 2, 3] for y in [4, 5, 6]])  # [5,6,7,6,7,8,7,8,9]

    # sets remove duplicates
    print({x + y for x in [1, 2, 3] for y in [4, 5, 6]})  # {5,6,7,9}
    print('')
    
    print({x: y for x in [1, 2, 3] for y in [4, 5, 6]})  # {1:4,2:5,3:6}
    print('')

    # set comprehension
    print({x + y for x in 'ab' for y in 'cd'})  # {'ac', 'ad', 'bc', 'bd'}
    
    # dictionary comprehension
    # {'ac':(97,99),'ad':(97,100),'bc':(98,99),'bd'(98,100)}
    print({x + y: (ord(x), ord(y)) for x in 'ab' for y in 'cd'})

    # set comprehension
    # {'spamspam','saussagesaussage'}
    print({k * 2 for k in ['spam', 'ham', 'saussage'] if k[0] == 's'})

    # dictionary comprehension
    # {'SPAM':'spamspam','SAUSSAGE':'saussage'}
    print({k.upper(): k * 2
           for k in ['spam', 'ham', 'saussage'] if k[0] == 's'})
