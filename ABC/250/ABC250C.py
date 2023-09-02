def calcAS(N, X):
    idx = []
    data = []
    for n in range(N):
        idx.append(n)
        data.append(n + 1)
    for x in X:
        # 該当する数字のindex
        i = idx[x - 1]
        if i < N - 1:
            # 該当するindexの取替対象のindex（右端にない場合）
            t = i + 1
        else:
            # 該当するindexの取替対象のindex（右端にある場合）
            t = i - 1
        # 該当する数字
        d = data[t]
        i2 = idx[d - 1]
        data[i], data[i2] = data[i2], data[i]
        idx[x - 1], idx[d - 1] = idx[d - 1], idx[x - 1]
    res = " ".join(map(str, data))
    print(res)


N, Q = [int(l) for l in input().split()]
x = []
for q in range(Q):
    x.append(int(input()))
calcAS(N, x)
