if __name__ == '__main__':
    print('code snippets from pages 270-271\n')
    rec = {}
    rec['name'] = 'Bob'
    rec['age'] = 40.5
    rec['job'] = 'developer/manager'
    print(rec)
    print(rec['name'])
    print('')

    # dictionary contains nested list and nested dictionary
    rec = {'name': 'Bob',
           'jobs': ['developer', 'manager'],
           'web': 'www.bobs.org/~Bob',
           'home': {'state': 'Overworled', 'zip': 12345}}
    print(rec)
    print(rec['name'])  # Bob
    print(rec['jobs'])  # nested list
    print(rec['jobs'][1])  # manager... second element in nested list
    print(rec['home']['zip'])  # 12345... index into nested dictionary
    print('')

    db = []  # empty list
    db.append(rec)  # list contains a single dictionary
    print(db)
    print(db[0]['jobs'])  # use key to access nested list
    print('')

    db = {}  # empty dictionary
    db['bob'] = rec  # dictionary contains a single key that is a dictionary
    print(db)
    print(db['bob']['jobs'])  # access nested list
    print(db['bob']['jobs'][1])  # access second item in nested list
