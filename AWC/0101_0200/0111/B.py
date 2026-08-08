from math import gcd

N, M = map(int, input().split())
S = list(map(int, input().split()))
S.sort()
T = []
for s in S:
    T.append(s)
for s in S:
    T.append(360 + s)
res = 10**18
for idx in range(M):
    l = T[idx]
    r = T[idx + M - 1]
    mid = (r - l) // 2
    res = min(res, max((r-l)-mid,mid-l))
d = 360 * res
g = gcd(d, N)
print(f"{d//g}/{N//g}")
