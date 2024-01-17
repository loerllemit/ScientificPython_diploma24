import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        return f"Elapsed time: {elapsed_time} seconds"
    return wrapper

@timer
def my_f(t=3):
    return time.sleep(t)

print(my_f())