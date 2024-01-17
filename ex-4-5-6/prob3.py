#%%
import numpy as np


def check_arr(func):
    def wrapper(*args, **kwargs):
        if args[0].size > 0 : 
            return func(*args, **kwargs)
        else:
            return "array is empty."
    return wrapper

@check_arr
def my_f(arr):
    return arr


arrs = np.array([1,2])
print('array:', arrs)
print(my_f(arrs))

arrs = np.array([])
print('array:', arrs)
print(my_f(arrs))
# %%
