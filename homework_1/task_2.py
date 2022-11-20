import psutil
import functools


def used_virtual_memory(f):
    @functools.wraps(f)
    def virtual_memory_check(*args, **kwargs):
        before_func = psutil.virtual_memory().available
        result = f(*args, **kwargs)
        after_func = psutil.virtual_memory().available
        used_memory = before_func - after_func
        print (f'Функція "{f.__name__}" використала {psutil._common.bytes2human(used_memory)} памяті')
        return result

    return virtual_memory_check
