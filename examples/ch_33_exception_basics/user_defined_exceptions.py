# user-defined exceptions are coded with classes that inherit from a built-in
# exception class (usually Exception)
class AlreadyGotOne(Exception):
    pass


def grail():
    raise AlreadyGotOne()  # raise an instance


# NOTE: user-defined exceptions can customize their error message by
# overloading their __str__() method
class Career(Exception):
    def __str__(self):
        return 'So I became a waiter...'


if __name__ == '__main__':
    print('code snippets from page 1125\n')
    try:
        grail()  # raises AlreadyGotOne
    except AlreadyGotOne:
        print('caught exception')
    print('')

    try:
        raise Career()
    except Exception as ex:
        print(ex)  # So I became a waiter... calls ex's __str__() method
    print('')
