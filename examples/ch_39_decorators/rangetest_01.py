# use as a decorator to perfrom simple range-testing for positional arguments
def rangetest(*argchecks):
    def on_decorator(func):
        if not __debug__:
            return func
        else:
            def on_call(*args):
                for (i, low, high) in argchecks:
                    if args[i] < low or args[i] > high:  # validate range
                        errmsg = 'Argument %s not in %s..%s' % (i, low, high)
                        raise TypeError(errmsg)
                return func(*args)  # return result of call
            return on_call  # return on_call handle
    return on_decorator  # return decorator handle
