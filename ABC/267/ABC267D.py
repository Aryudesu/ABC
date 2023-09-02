INF = -10**18
N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
res = 0
m = 1
for a in A:
    if a > 0:
        res += m * a
        m += 1
