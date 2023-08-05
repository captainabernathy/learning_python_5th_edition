trace_me = False


def trace(*args):
    if trace_me:
        print('[' + ' '.join(map(str, args)) + ']')


# mixin class that reroutes operator overloading methods to a subclass...
# used as a superclass to access_control() proxy class... assumes the proxy
# has a _wrapped attribute
class BuiltinsMixin:
    def __add__(self, rhs):
        return self._wrapped + rhs

    def __str__(self):
        return str(self._wrapped)

    def __getitem__(self, i):
        return self._wrapped[i]

    def __call__(self, *args, **kargs):
        return self._wrapped(*args, **kargs)


def access_control(fail_if):
    def on_decorator(acls):
        class on_instance(BuiltinsMixin):
            def __init__(self, *args, **kwargs):
                # uses __X pseudoprivate name mangling to localize the wrapped
                # attribute to the proxy control class (by automatically
                # prefixing it with this class's name)
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

