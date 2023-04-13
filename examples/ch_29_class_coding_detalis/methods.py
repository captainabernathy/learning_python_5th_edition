class NextClass:
    def printer(self, text):
        self.message = text  # update instance
        print(self.message)  # access instance


if __name__ == '__main__':
    print('code snippets from pages 891-892\n')
    x = NextClass()  # make instance

    # NOTE: when an object calls a method, python automatically passes the
    # first argument to self
    x.printer('instance call')  # instance call... call x's printer method
    print(x.message)  # instance call... access x's message attribute
    print('')

    # direct call... passing x to self... updates x
    NextClass.printer(x, 'class call')  # class call
    print(x.message)  # class call
    # NextClass.printer('bad call')  # TypeError... method called w/o instance
