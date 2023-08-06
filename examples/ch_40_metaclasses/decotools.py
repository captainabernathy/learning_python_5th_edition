import time


# can be used as a decorator to trace calls to func
def tracer(func):
    calls = 0

    def on_call(*args, **kargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, *kargs)

    return on_call


def timer(label='', trace=True):
    def on_decorator(func):

        def on_call(*args, **kargs):
            start = time.time()
            result = func(*args, **kargs)
            elapsed = time.time() - start
            on_call.alltime += elapsed

            if trace:
                format = '%s%s: %0.10f, %0.10f'
                values = (label, func.__name__, elapsed, on_call.alltime)
                print(format % values)

            return result

        on_call.alltime = 0

        return on_call

    return on_decorator
