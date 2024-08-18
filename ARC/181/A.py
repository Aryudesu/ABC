T = int(input())
result = []
for _ in range(T):
    N = int(input())
    P = [int(l) for l in input().split()]
    mx = -1
    mn = N + 1
    alr_f = True
    ok_f = False
    for idx in range(N):
        p = P[idx]
        mx = max([p, mx])
        mn = min([p, mn])
        # print(p, mx, mn)
        if idx + 1 != p:
            alr_f = False
        if idx + 1 == p and p == mx and mn == 1:
            ok_f = True
    if alr_f:
        result.append(0)
    elif ok_f:
        result.append(1)
    elif P[0] != N or P[-1] != 1:
        result.append(2)
    else:
        result.append(3)
# print(result)
for r in result:
    print(r)
