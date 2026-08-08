N, K = map(int, input().split())
A = list(map(int, input().split()))
if K == 0:
    if 0 in A:
        print(A.count(0))
    else:
        print(-1)
else:
    count = 0
    res = 0
    for a in A:
        tmp = a
        k = K
        f = True
        while tmp:
            if not (k & 1) and (tmp & 1):
                f = False
                break
            k >>= 1
            tmp >>= 1
        if f:
            res |= a
            count += 1
    if res == K:
        print(count)
    else:
        print(-1)
