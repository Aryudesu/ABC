def eratosthenes(N: int)->list[int]:
    """エラトステネスの篩"""
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    primes = [2] if N >= 2 else []
    for i in range(3, N + 1, 2):
        if not is_prime[i]:
            continue
        primes.append(i)
        if i * i > N:
            continue
        for j in range(i * i, N + 1, 2 * i):
            is_prime[j] = False
    return primes


def soinsu(n: int, primes: list[int])->dict[int, int]:
    """Nの素因数分解"""
    tmp = n
    result = dict()
    for p in primes:
        if tmp % p == 0:
            while True:
                if tmp % p != 0:
                    break
                result[p] = result.get(p, 0) + 1
                tmp //= p
        elif p * p > tmp:
            result[tmp] = result.get(tmp, 0) + 1
            return result
    return result

def sortedInsert(data: list, num: int):
    """ソート形式で挿入"""
    tmp1, tmp2 = data
    # 最大更新
    if tmp2 <= num:
        data[0] = tmp2
        data[1] = num
        return
    # 2番目の値更新
    if tmp1 <= num:
        data[0] = num
        return


def calc(primes: list[int])->list[int]:
    """計算"""
    N = int(input())
    A = list(map(int, input().split()))
    expData = dict()
    soinsuData = []
    for a in A:
        peData = soinsu(a, primes)
        soinsuData.append(peData)
        for p, e in peData.items():
            tmp = expData.get(p, [0, 0])
            sortedInsert(tmp, e)
            expData[p] = tmp
    lcm = 1
    for p, elist in expData.items():
        lcm = (lcm * pow(p, elist[-1], MOD)) % MOD
    result = []
    for i in range(N):
        factData = soinsuData[i]
        inv = 1
        for p, e in factData.items():
            lcmE = expData[p]
            if lcmE[-1] == e:
                diff = lcmE[1] - lcmE[0]
                inv_pe = pow(pow(p, diff, MOD),  MOD-2, MOD)
                inv = (inv * inv_pe) % MOD
        result.append((lcm * inv) % MOD)
    return result


MOD = 998244353
primes = eratosthenes(10000)
T = int(input())
for _ in range(T):
    res = calc(primes)
    print(*res)
