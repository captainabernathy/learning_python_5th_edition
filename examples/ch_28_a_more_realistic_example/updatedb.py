import shelve

if __name__ == '__main__':
    print('code snippet from page 881\n')
    db = shelve.open('persondb')  # open shelve

    # output data in shelve
    for key in sorted(db):
        print(key, '\t=>', db[key])

    sue = db['Sue Jones']  # get stored object
    sue.give_raise(.10)  # updated retrieved object
    db['Sue Jones'] = sue  # write updated object back to db
    db.close()
