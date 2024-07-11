from functools import lru_cache


@lru_cache(maxsize=256)
def f(num):
    if num == 0:
        return 1
    return f(num//2) + f(num//3)


print(f(int(input())))
