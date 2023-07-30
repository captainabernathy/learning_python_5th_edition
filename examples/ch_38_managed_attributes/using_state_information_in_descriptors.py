# NOTE: this Descriptor class manages data both instances of itself and on
# client instances

class DescBoth:
    # constructor builds a DescBoth with its data member initialized to data
    def __init__(self, data):
        self.data = data

    # returns a string that is formated to display this DescBoth's data
    # attribute and instance's data attribute
    def __get__(self, instance, owner):
        return '%s, %s' % (self.data, instance.data)

    # sets instance's data attribute to value
    def __set__(self, instance, value):
        instance.data = value


class Client:
    # constructor builds a Client with its data member initialized to data
    def __init__(self, data):
        self.data = data

    # assigns a DescBoth descriptor initialized to 'spam' to the attribute
    # managed
    managed = DescBoth('spam')


if __name__ == '__main__':
    print('code snippets from page 1277\n')

    Ins = Client('eggs')
    print(Ins.managed)  # spam, eggs
    print('')

    Ins.managed = 'SPAM'  # sets Ins's data attribute
    print(Ins.managed)  # spam, SPAM
    print('')

    print(Ins.__dict__)  # {'data': 'SPAM'}
    print('')

    # ['data', 'managed']
    print([x for x in dir(Ins) if not x.startswith('__')])
    print('')

    print(getattr(Ins, 'data'))  # 'SPAM'
    print('')

    print(getattr(Ins, 'managed'))  # spam, SPAM
    print('')

    # data => SPAM
    # managed => spam, SPAM
    for attr in (x for x in dir(Ins) if not x.startswith('__')):
        print('%s => %s' % (attr, getattr(Ins, attr)))
    print('')
