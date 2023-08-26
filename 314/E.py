N, M = [int(l) for l in input().split()]
CPS = dict()
PS = set()
for n in range(N):
    C, P, *S = [int(l) for l in input().split()]
    for s in S:
        tmp = CPS.get(s, 0)
        tmp += C/P
        CPS[s] = tmp
        PS.add(s)
PS = list(PS)
PS.sort()
dp = [0]*(M + PS[-1] + 1)
for m in range(M):
    for ps in PS:
        dp[m + ps] += CPS[ps] + dp[m]
print(CPS)
print(dp)
result = 0
for m in range(M, len(dp)):
    result += dp[m]
print(result)
