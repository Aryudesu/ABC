def calc(N: int, M: int, D: list[int])->int:
    MOD = 998244353
    data1 = set()
    maxNum = 0
    result2 = 1
    # 0が入っているインデックス達
    zeroIndexes = []
    # 0以外が入らないといけないものに値を入れていく
    for idx in range(N):
        d = D[idx]
        if d:
            if maxNum + 1 >= d:
                data1.add(d)
                maxNum = min(N, max(maxNum, d))
            else:
                count = 0
                while d - count > maxNum + 1:
                    if len(zeroIndexes) == 0:
                        return 0
                    i = zeroIndexes.pop()
                    count += 1
                    D[i] = d - count
        else:
            zeroIndexes.append(idx)

    maxNum = 0
    for idx in range(N):
        d = D[idx]
        if d:
            if d > M:
                return 0
            if maxNum + 1 >= d:
                data1.add(d)
                maxNum = min(N, max(maxNum, d))
            else:
                return 0
        else:
            result2 = (result2 * M) % MOD

    result1 = 1
    for i in range(len(data1)):
        result1 = (result1 * (M - i)) % MOD

    print(result1, result2)
    print(D)
    return (result1 * result2) % MOD


N, M = map(int, input().split())
D = list(map(int, input().split()))
res = calc(N, M, D)
print(res)
