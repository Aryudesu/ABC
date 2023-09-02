def p_fact(N):
    """素因数分解"""
    num = N
    res = dict()
    while True:
        if num % 2 == 0:
            tmp = res.setdefault(2, 0)
            res[2] = tmp + 1
            num //= 2
        else:
            break
    for idx in range(3, N + 1, 2):
        if num % idx != 0 and idx ** 2 > num:
            if num != 1:
                res[num] = 1
            break
        while True:
            if num % idx == 0:
                tmp = res.setdefault(idx, 0)
                res[idx] = tmp + 1
                num //= idx
            else:
                break
    return res


def calc_min(N, V):
    count = 0
    res = 0
    num = 0
    for v in range(V):
        res += 1
        num += N
        tmp = num
        while True:
            if tmp % N == 0:
                tmp //= N
                count += 1
            else:
                break
        if V <= count:
            break
    return res


K = int(input())
fact = p_fact(K)
res = 1
for k, v in fact.items():
    n = calc_min(k, v)
    if res < k * n:
        res = k * n
print(res)
