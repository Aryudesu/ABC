def p_calc(N):
    result = [True] * (N + 1)
    primes = [2]
    for i in range(3, N + 1, 2):
        if not result[i]:
            continue
        primes.append(i)
        idx = 3
        while idx * i <= N:
            result[idx * i] = False
            idx += 2
    return primes


primes = p_calc(50000)


def yakusu(N):
    """Nの約数の個数計算"""
    tmp = N
    result = set()
    # 各素数で走査
    for p in primes:
        if tmp % p == 0:
            result.add(p)
            # 割れるだけ割る
            while True:
                if tmp % p != 0:
                    break
                tmp //= p
        if tmp == 1:
            break
        if p * p > tmp:
            result.add(tmp)
            break
    return result


T = int(input())
result = []
for t in range(T):
    N = int(input())
    res = yakusu(N)
    if len(res) == 1:
        result.append("No")
    else:
        result.append("Yes")
for r in result:
    print(r)
