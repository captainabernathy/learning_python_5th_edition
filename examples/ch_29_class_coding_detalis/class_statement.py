class SharedData:
    spam = 42  # generates a class data attribute


class MixedNames:
    data = 'spam'   # class attribute

    def __init__(self, value):
        self.data = value

    def display(self):
        print(self.data, MixedNames.data)  # show instance attr and class attr


if __name__ == '__main__':
    print('code snippets from pages 889-890\n')
    x = SharedData()
    y = SharedData()
    print(x.spam, y.spam)  # 42 42... both share spam
    print('')

    SharedData.spam = 99  # changes class attribute
    print(x.spam, y.spam, SharedData.spam)  # 99 99 99
    print('')

    # NOTE: assignments to instance attributes create or change the named
    # attribute in the instance... NOT in the shared class
    x.spam = 88  # only changes x's spam attribute
    print(x.spam, y.spam, SharedData.spam)  # 88 99 99
    print('')

    x = MixedNames(1)
    y = MixedNames(2)
    x.display()  # 1 spam
    y.display()  # 2 spam
