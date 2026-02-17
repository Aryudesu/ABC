def eratosthenes(N: int):
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


def soinsu(n: int, primes: list[int]):
    """Nの素因数分解"""
    tmp = n
    idx = 0
    result = []
    while tmp > 1:
        p = primes[idx]
        if tmp % p == 0:
            count = 0
            while True:
                if tmp % p != 0:
                    result.append((p, count))
                    break
                count += 1
                tmp //= p
        elif p * p > tmp:
            result.append((tmp, 1))
            return result
        idx += 1
    return result

def sortedInsert(data: list, num: int):
    """ソート形式で挿入"""
    # 長さ0のときの更新
    if len(data) == 0:
        data.append(num)
        return
    # 長さ1のときの更新
    if len(data) == 1:
        tmp = data[0]
        # 最大更新（同じ値）
        if num == tmp:
            data.append(num)
            return
        # 最大更新（異なる値）
        elif num < tmp:
            data.append(0)
            data[0] = num
            data[1] = tmp
            return
        # 最大更新（2番めの値）
        elif num > tmp:
            data.append(0)
            data[0] = tmp
            data[1] = num
            return
        return
    # 長さ2のときの更新
    if len(data) == 2:
        tmp1 = data[0]
        tmp2 = data[1]
        # 最大更新
        if tmp2 <= num:
            data[0] = tmp2
            data[1] = num
            return
        # 2番目の値更新
        if tmp1 <= num:
            data[0] = num
            return

MOD = 998244353
primes = eratosthenes(10000)
inv_memo = dict()
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    data = dict()
    lcmMemo = dict()
    soinsuData = []
    # 各値を素因数分解する
    for a in A:
        peData = soinsu(a, primes)
        soinsuData.append(peData)
        for p, e in peData:
            # 指数情報更新
            tmp = data.get(p, [])
            sortedInsert(tmp, e)
            data[p] = tmp
            # 最小公倍数の計算用に最大指数を計算
            lcmMemo[p] = max(lcmMemo.get(p, 0), e)
    # 最小公倍数計算
    lcm = 1
    for p in lcmMemo:
        e = lcmMemo[p]
        lcm = (lcm * pow(p, e, MOD)) % MOD
    # 各値について計算
    result = []
    for i in range(N):
        # 素因数分解情報
        peData= soinsuData[i]
        # 最小公倍数
        lcm_tmp = lcm
        # 必要な逆数計算
        inv=1
        for p, e in peData:
            lcmE = data[p]
            # 最大の指数がeであるときは更新対象
            if lcmE[-1] == e:
                # それしか無いならそれを除外する
                if len(lcmE) == 1:
                    inv_p = pow(p, MOD-2, MOD)
                    inv_pe = pow(inv_p, e, MOD)
                    inv = (inv * inv_pe) % MOD
                # 二番手があるならそれにする
                elif len(lcmE) == 2:
                    if lcmE[1] != lcmE[0]:
                        inv_p = pow(p, MOD-2, MOD)
                        inv_pe = pow(inv_p, lcmE[1] - lcmE[0], MOD)
                        inv = (inv * inv_pe) % MOD
        # 逆数をかける
        result.append((lcm * inv) % MOD)
    print(*result)
