def calc(L, S, R, idx, d):
    if L * 2 >= R:
        return d + 1
    for i in range(idx, len(S)):
        s = S[i]
        if s > L * 2:
            if idx == i:
                return -1
            else:
                return calc(S[i-1], S, R, i, d+1)
    if len(S) > 0:
        if S[-1] * 2 >= R:
            return d + 2
    return -1

T = int(input())
result = []
for t in range(T):
    N = int(input())
    L, *S = [int(l) for l in input().split()]
    R = S[-1]
    S.pop()
    S.sort()
    result.append(calc(L, S, R, 0, 1))
for r in result:
    print(r)
