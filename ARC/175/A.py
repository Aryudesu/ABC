N = int(input())
P = [int(l) - 1 for l in input().split()]
S = input()
MOD = 998244353
# 左
LCount = 1
LData = [False] * N
for idx in range(N):
    p = P[idx]
    s = S[p]
    if s == "L":
        pass
    elif s == "R":
        if not LData[(p + 1) % N]:
            LCount *= 0
    elif s == "?":
        if LData[(p + 1) % N]:
            LCount = (2 * LCount) % MOD
    LData[p] = True
# 右
RCount = 1
RData = [False] * N
for idx in range(N):
    p = P[idx]
    s = S[p]
    if s == "R":
        pass
    elif s == "L":
        if not RData[(p - 1) % N]:
            RCount *= 0
    elif s == "?":
        if RData[(p - 1) % N]:
            RCount = (2 * RCount) % MOD
    RData[p] = True
print((LCount + RCount) % MOD)
