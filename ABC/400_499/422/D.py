from functools import cache

import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

RESULT = []
@cache
def calc(num, depth):
    """返却値は 配列データ, アンバランスさ"""
    n = num // 2
    if depth == 1:
        M = max(n, num - n)
        m = min(n, num - n)
        return [n, num - n], M - m
    res1, amb1 = calc(n, depth - 1)
    res2, amb2 = calc(num - n, depth - 1)
    amb3 = abs(num - n - n)
    return [res1, res2], max(amb1, amb2, amb3)


def make_print_data(data):
    if type(data) is list:
        for d in data:
            make_print_data(d)
    else:
        RESULT.append(data)

N, K = [int(l) for l in input().split()]
data, amb = calc(K, N)
make_print_data(data)
print(amb)
print(*RESULT)
