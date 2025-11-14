from functools import lru_cache

@lru_cache(maxsize=1000)
def calc(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    return calc(n-1) + calc(n-2)

for i in range(1, 101):
    print(f"羊が{calc(i)}匹")
