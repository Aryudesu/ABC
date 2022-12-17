import time


def calc_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, time.time() - start)
        return result
    return wrapper


@calc_time
def calc(num):
    for i in range(num):
        time.sleep(1)
    return 100


print(calc(3))
