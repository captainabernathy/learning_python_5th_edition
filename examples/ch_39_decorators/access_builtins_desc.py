# a mixin class that contains a nested proxy class that is used to generate
# methods from a list of names and intercept only the attribute fetch that
# precedes the call
class BuiltinsMixin:
    class ProxyDesc(object):
        def __init__(self, attr):
            self.attr = attr

        def __get__(self, instance, owner):
            return getattr(instance._wrapped, self.attr)

    builtins = ['add', 'str', 'getitem', 'call']

    for attr in builtins:
        exec('__%s__ = ProxyDesc("__%s__")' % (attr, attr))
