import time


def timer(label='', trace=True):  # runs on @timer decorator, args: retain args
    class Timer:
        def __init__(self, func):  # runs on @: retain decorated func
            self.func = func
            self.alltime = 0

        def __call__(self, *args, **kwargs):  # runs on calls: call original fn
            start = time.time()
            result = self.func(*args, **kwargs)
            elapsed = time.time() - start
            self.alltime += elapsed
            if trace:
                format = '%s %s: %.5f, %.5f'
                values = (label, self.func.__name__, elapsed, self.alltime)
                print(format % values)
            return result
    return Timer
