# usage: python3 withas.py

class TraceBlock:
    '''
    TraceBlock provides a context manager that can be use to trace the entry
    and exit of a with block in any with statement
    '''
    def message(self, arg):
        print('running ' + arg)

    def __enter__(self):
        print('starting with block')
        return self  # self gets assigned to as object

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('exited normally\n')
        else:
            print('raise an exception: ' + str(exc_type))
            return False  # propagates/reraises exception


if __name__ == '__main__':
    # Context Management Protocol:
    #   1. the expression that follows 'with' must have __enter__() and
    #      __exit__() methods
    #
    #   2. the context manager's __enter__() method is classed, and the value
    #      it return is (optionally) assigned to the variable in the as clause
    #      if one is provided
    #
    #   3. the code in the with block is executed
    #
    #   4. if the with block raises an exception, its __exit__() method is
    #      called with the exception details provided
    #
    #   5. if the with block does not raise an exception, its __exit__() method
    #      is still called, but its type, value, and traceback arguments are
    #      all passed as None

    print('code snippets from pages 1155-1156\n')

    with TraceBlock() as action:  # starting with block
        action.message('test 1')  # running test 1
        print('reached')
        # exited normally

    with TraceBlock() as action:  # starting with block
        action.message('test 2')  # running test 2
        raise TypeError  # raise an exception: <class 'TypeError'>
        print('not reached')
