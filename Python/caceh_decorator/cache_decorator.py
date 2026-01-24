import time
from functools import wraps

def cache(func):
    '''decorator function'''
    catch_value = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        if args in catch_value:
            return catch_value[args]
        result = func(*args, **kwargs)
        catch_value[args] = result
        return result
    return wrapper

@cache  #decorator
def long_exe_fun(a,b,c,d,e):
    time.sleep(4)
    return a/b*c+d-e

print(long_exe_fun(10,2,3,4,2))
print(long_exe_fun(10,2,3,4,2))
print(long_exe_fun(20,4,6,8,4))
print(long_exe_fun(20,4,6,8,4))
print(long_exe_fun(20,4,6,8,4))
print(long_exe_fun(20,4,6,8,4))