N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]

SA = [0]
sa = 0
SSA = [0]
ssa = 0
for n in range(N):
    sa += A[n]
    ssa += A[n] * (n+1)
    SA.append(sa)
    SSA.append(ssa)
res = -10**10000
for n in range(M, N+1):
    tmp = (SSA[n] - SSA[n-M]) - (SA[n] - SA[n-M]) * (n - M)
    if res < tmp:
        res = tmp
print(res)
