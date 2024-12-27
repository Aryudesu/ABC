def updateData(left: dict, right: dict, keta: int, B: int, MOD: int):
    result = dict()
    for idx1 in left:
        for idx2 in right:
            n1 = left.get(idx1, 0)
            n2 = right.get(idx2, 0)
            if n1 == 0 or n2 == 0:
                continue
            m = (idx1 * (10 ** keta) + idx2) % B
            result[m] = (result.get(m, 0) + n1 * n2) % MOD
    return result


def calc(N, B, C):
    num = N
    MOD = 10 ** 9 + 7
    # 計算用
    result = dict()
    # 各桁用
    keta = 1
    # keta[2のべき乗桁についてBで割った余り] = 通り数
    ketaData = dict()
    for c in C:
        k = c % B
        ketaData[k] = (ketaData.get(k, 0) + 1) % MOD
    while num % 2 == 0:
        ketaData = updateData(ketaData, ketaData, keta, B, MOD)
        keta *= 2
        num >>= 1
    for k in ketaData:
        result[k] = ketaData[k]
    num >>= 1
    while num:
        ketaData = updateData(ketaData, ketaData, keta, B, MOD)
        keta *= 2
        if num % 2:
            result = updateData(result, ketaData, keta, B, MOD)
        num >>= 1
    return result.get(0, 0)


N, B, K = [int(l) for l in input().split()]
C = [int(l) % B for l in input().split()]
print(calc(N, B, C))
