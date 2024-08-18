RESULT = []
dat = []

def calc(depth, dat, S, N, K, R):
    if depth == N:
        if S % K == 0:
            RESULT.append(tuple(dat))
        return
    Rd = R[depth]
    for r in range(1, Rd + 1):
        dat[depth] = r
        calc(depth + 1, dat, S + r, N, K, R)

N, K = [int(l) for l in input().split()]
dat = [0] * N
R = [int(l) for l in input().split()]
calc(0, dat, 0, N, K, R)
RESULT.sort()
for r in RESULT:
    print(*r)
