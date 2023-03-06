if __name__ == '__main__':
    print('code snippets from pages 116-117\n')
    D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
    print(D)  # {'food':'Spam',...,'color':'pink'}

    # index by key
    print(D['food'])  # Spam

    # update dictionary in place
    D['quantity'] += 1
    print(D['quantity'])  # 5

    print(D)

    # create a dictionary from scratch
    D = {}
    D['name'] = 'Bob'
    print(D)  # {'name':'Bob'}

    D['job'] = 'dev'
    print(D)  # {'name':'Bob', 'job':'dev'}

    D['age'] = 40
    print(D)  # {'name':'Bob', 'job':'dev', 'age':40}

    # use dict() function with key=value pairs to construct a dictionary
    bob1 = dict(name='Bob', job='dev', age=40)
    print(bob1)  # {'name':'Bob', 'job':'dev', 'age':40}

    # alternatively use the zip() function to combine a list keys with a list
    # of values
    bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
    print(bob2)  # {'name':'Bob', 'job':'dev', 'age':40}
