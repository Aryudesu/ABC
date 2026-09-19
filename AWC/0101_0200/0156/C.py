INF = 10 ** 18

def isOk(N: int, K: int, A: list[int], mid: int)->int:
    c = 1
    m = A[0]
    res = 0
    tmp = 0
    for n in range(N):
        a = A[n]
        if a - m > mid:
            c += 1
            m = a
            tmp = 0
            res += tmp
        tmp = max(a - m, tmp)
        if c > K:
            return False
    return res if c <= K else INF

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
print(A)
l = 0
r = A[-1]
while r - l > 1:
    mid = (r + l) // 2
    if isOk(N, K, A, mid):
        r = mid
    else:
        l = mid
print(r)
