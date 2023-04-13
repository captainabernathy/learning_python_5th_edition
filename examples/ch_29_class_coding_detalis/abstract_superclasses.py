class Super:
    def delegate(self):
        self.action()

    def action(self):  # assert subclass must define action
        assert False, 'action must be defined'


class Sub(Super):
    def action(self):  # rasie exception... expect subclass to define action
        raise NotImplementedError('action must be implemented!')


if __name__ == '__main__':
    print('code snippets from pages 898-899\n')
    X = Super()  # build a Super instance
    try:
        X.delegate()
    except AssertionError as err:
        print('AssertionError:', err)  # AssertionError: action must be defined

    Y = Sub()  # build a Sub instance
    try:
        Y.action()
    except NotImplementedError as err:
        # NotImplementedError: action must be implemented!
        print('NotImplementedError:', err)
