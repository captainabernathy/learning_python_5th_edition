# usage: python3 display_usage_notes.py

class Printer1:
    def __init__(self, val):
        self.val = val

    # used for instance itself
    # convert to string
    def __str__(self):
        return str(self.val)


class Printer2:
    def __init__(self, val):
        self.val = val

    # used by print if no __str__()...
    # used if echoed or nested
    def __repr__(self):
        return str(self.val)


if __name__ == '__main__':
    print('code snippets from page 945\n')

    objs = [Printer1(2), Printer1(3)]
    for x in objs:
        print(x)  # 2 3... __str__() run when instance printed
    print('')

    print(objs)  # [<__main__.Printer1 object..>,<__main__.Printer1 object..>]
                 # __str__() NOT used when instance is a list
    print('')

    objs = [Printer2(2), Printer2(3)]
    for x in objs:
        print(x)  # 2 3... no __str__()... calls __repr__()... returns str()
    print('')

    print(objs)  # [2, 3]... no __str__()... calls __repr__()... returns str()
