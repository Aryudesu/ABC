from math import lcm

N, M = map(int, input().split())
P = list(map(int, input().split()))
res = 1
isOk = True
for p in P:
    res = lcm(res, p)
    if res > M:
        isOk = False
        break
print("Yes" if isOk else "No")
