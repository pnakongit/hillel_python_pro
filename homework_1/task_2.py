import psutil
import functools


def used_virtual_memory():
    def internal(f):
        @functools.wraps(f)
        def virtual_memory_check(*args, **kwargs):
            before_func = psutil.virtual_memory().available
            result = f(*args, **kwargs)
            after_func = psutil.virtual_memory().available
            print(f'Було викрористано байт памяті: {before_func - after_func}')
            return result

        return virtual_memory_check

    return internal
