import functools
import requests


def cache(max_limit=3):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))

            if cache_key in dict_cache:
                counter_cache[cache_key] += 1
                return dict_cache[cache_key]

            result = f(*args, **kwargs)

            if len(dict_cache) >= max_limit:
                print('!!!!!!')
                min_count = min(counter_cache, key=counter_cache.get)
                dict_cache.pop(min_count)

            dict_cache[cache_key] = result
            counter_cache[cache_key] = 1
            print(dict_cache)
            print(len(dict_cache))
            return result

        dict_cache, counter_cache = {}, {}
        return deco

    return internal


@cache()
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content