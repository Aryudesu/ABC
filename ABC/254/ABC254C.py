import bisect

def calc(A, Aft, N, K):
    f = [True for n in range(N)]
    for idx in range(N):
        num = A[idx]
        nidx = bisect.bisect_left(Aft, num)
        if (nidx - idx) % K:
            nidx += K - (nidx - idx) % K
        if nidx >= N:
            return False
        for k in range(N//K + 1):
            if Aft[nidx] == num and f[nidx]:
                f[nidx] = False
                break
            nidx += K
            if nidx > N or num != Aft[nidx]:
                return False
    return True


N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
A_aft = sorted(A)
if calc(A, A_aft, N, K):
    print('Yes')
else:
    print('No')
