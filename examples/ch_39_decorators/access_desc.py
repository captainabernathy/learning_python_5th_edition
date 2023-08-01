from access_builtins_desc import BuiltinsMixin

trace_me = False


def trace(*args):
    if trace_me:
        print('[' + ' '.join(map(str, args)) + ']')


def access_control(fail_if):
    def on_decorator(acls):
        if not __debug__:
            return acls
        else:
            class on_instance(BuiltinsMixin):
                def __init__(self, *args, **kwargs):
                    self._wrapped = acls(*args, **kwargs)

                def __getattr__(self, attr):
                    trace('get:', attr)
                    if fail_if(attr):
                        raise TypeError('private attribute fetch: ' + attr)
                    else:
                        return getattr(self._wrapped, attr)

                def __setattr__(self, attr, value):
                    trace('set:', attr, value)
                    if attr == '_wrapped':
                        self.__dict__[attr] = value
                    elif fail_if(attr):
                        raise TypeError('private attribute change: ' + attr)
                    else:
                        setattr(self._wrapped, attr, value)
            return on_instance
    return on_decorator


# use as annotation to set private attributes
def private(*attributes):
    return access_control(fail_if=(lambda attr: attr in attributes))


# use as annotation to set public attributes
def public(*attributes):
    return access_control(fail_if=(lambda attr: attr not in attributes))

