'''
File rangetest.py: provides a function decorator that performs range testing
validation for arguments passed to any function or method.

Arguments should be specified by keyword to the decorator. In subsequent calls,
arguments may be passed by position or keyword, and defaults may be omitted.

See rangetest_test.py for examples.
'''

trace = True


def rangetest(**argchecks):
    def on_decorator(func):
        if not __debug__:
            return func
        else:
            code = func.__code__
            allargs = code.co_varnames[:code.co_argcount]
            funcname = func.__name__

            def on_call(*pargs, **kargs):
                expected = list(allargs)  # list of expected arguments
                # assume pargs match the first N args by position
                pos_args = expected[:len(pargs)]
                # loop over all arguments
                for (arg, (low, high)) in argchecks.items():
                    if arg in kargs:  # check for keyword args
                        if kargs[arg] < low or kargs[arg] > high:  # test range
                            errmsg = '{0} argument "{1}" not in {2}..{3}'
                            errmsg = errmsg.format(funcname, arg, low, high)
                            raise TypeError(errmsg)
                    elif arg in pos_args:  # check for positional args
                        pos = pos_args.index(arg)
                        if pargs[pos] < low or pargs[pos] > high:  # test range
                            errmsg = '{0} argument "{1}" not in {2}..{3}'
                            errmsg = errmsg.format(funcname, arg, low, high)
                            raise TypeError(errmsg)
                    else:  # assume default
                        if trace:
                            print('Argument "{0}" defaulted'.format(arg))
                return func(*pargs, **kargs)  # return result of call
            return on_call  # return on_call handle
    return on_decorator  # return on_decorator handle

