def calc(K1, K2, N):
    if K1 > K2:
        return 0
    res = 0
    K1_ = K1
    while K1 <= N:
        K1 *= 10
        res += 1
    if K1_ != K2:
        while K2 <= N:
            K2 *= 10
            res += 1
    return res


N, K1 = [int(l) for l in input().split()]
tmp = list(str(K1))
tmp.reverse()
tmp2 = "".join(tmp)
K2 = int(tmp2)
print(calc(K1, K2, N))
