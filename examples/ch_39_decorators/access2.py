trace_me = False


def trace(*args):
    if trace_me:
        print('[' + ' '.join(map(str, args)) + ']')


def access_control(fail_if):
    def on_decorator(acls):
        class on_instance:
            def __init__(self, *args, **kwargs):
                # uses __X pseudoprivate name mangling to localize the wrapped
                # attribute to the proxy control class (by automatically
                # prefixing it with this class's name)
                self.__wrapped = acls(*args, **kwargs)

            def __getattr__(self, attr):
                trace('get:', attr)
                if fail_if(attr):
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.__wrapped, attr)

            def __setattr__(self, attr, value):
                trace('set:', attr, value)
                # must use fully expanded name string _on_instance__wrapped
                if attr == '_on_instance__wrapped':
                    self.__dict__[attr] = value
                elif fail_if(attr):
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.__wrapped, attr, value)
        return on_instance
    return on_decorator


# use as annotation to set private attributes
def private(*attributes):
    return access_control(fail_if=(lambda attr: attr in attributes))


# use as annotation to set public attributes
def public(*attributes):
    return access_control(fail_if=(lambda attr: attr not in attributes))
