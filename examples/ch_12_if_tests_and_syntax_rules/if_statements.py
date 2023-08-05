# usage: python3 if_statements.py

if __name__ == '__main__':
    print('code snippets from pages 384-386\n')

    if 1:  # always true
        print('true')
    else:
        print('false')

    if not 1:  # never true
        print('true')
    else:
        print('false')
    print('')

    # NOTE: strings in python can be evaluated for equality
    x = 'killer rabbit'
    if x == 'roger':
        print('shave and a haircut')
    elif x == 'bugs':
        print("what's up doc")
    else:
        print('Run away! ' * 2)
    print('')

    choice = 'ham'
    print({'spam': 1.25,
           'ham': 1.99,
           'eggs': 0.99,
           'bacon': 1.10}[choice])  # 1.99... dictionary-based 'switch'

    # ^^^ is the same as
    if choice == 'spam':
        print(1.25)
    elif choice == 'ham':
        print(1.99)
    elif choice == 'eggs':
        print(0.99)
    elif choice == 'bacon':
        print(1.10)
    else:
        print('Bad choice')

    # similarly...
    branch = {'spam': 1.25, 'ham': 1.99, 'eggs': 0.99}
    # NOTE: a dictionary's get() method will return None if unsuccessful and
    # no alternative has been provided
    print(branch.get('ham', 'Bad choice'))  # 1.99
    print(branch.get('bacon', 'Bad choice'))  # Bad choice
    print(branch.get('bacon'))  # None

    # likewise...
    # NOTE: dictionary keys can be evaluated for equality
    choice = 'ham'
    if choice in branch:
        print(branch[choice])
    else:
        print('Bad choice')

    choice = 'bacon'
    if choice in branch:
        print(branch[choice])
    else:
        print('Bad choice')
