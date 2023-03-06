import json

if __name__ == '__main__':
    print('code snippets from pages 300-301\n')

    name = dict(first='Bob', last='Smith')
    rec = dict(name=name, job=['dev', 'mgr'], age=40.5)
    print(rec)
    print('')

    # the json module's dumps() function translates a python object to json
    print(json.dumps(rec))
    print('')

    S = json.dumps(rec)
    # the json module's loads() function translates json to python
    L = json.loads(S)
    print(L)
    print(L == rec)  # True
    print('')

    # the json module's dump() function converts a python object to json and
    # writes it to a file
    json.dump(rec, fp=open('testjson.txt', 'w'), indent=4)
    
    print(open('testjson.txt').read())
