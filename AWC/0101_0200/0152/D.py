def calc(N: int, S: int, P: list[int])->int:
    M = N // 2
    L = N - M
    counter = 0
    mData = dict()
    for mask in range(1 << M):
        tmp = 0
        for m in range(M):
            b = 1 << m
            if mask & b:
                tmp += P[m]
        if tmp <= S:
            mData[tmp] = mData.get(tmp, 0) + 1
    for mask in range(1 << L):
        tmp = 0
        for l in range(L):
            b = 1 << l
            if mask & b:
                tmp += P[M + l]
        if S-tmp in mData:
            counter += mData[S-tmp]
            if counter >= 2:
                return 2
    return counter



N, S = map(int, input().split())
P = list(map(int, input().split()))
res = calc(N, S, P)
if res == 2:
    print("YES")
elif res == 1:
    print("ALMOST")
elif res == 0:
    print("NO")
else:
    raise ValueError()
