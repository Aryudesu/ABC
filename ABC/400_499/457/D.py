def isOk(mid: int, A: list[int], K: int)->bool:
    k = 0
    for n in range(N):
        a = A[n]
        if mid > a:
            if k > K:
                return False
            k += (mid - a + n) // (n + 1)
    return k <= K

N, K = map(int, input().split())
A = list(map(int, input().split()))
r = 2 * (10**32) + 1
l = -1
while r - l > 1:
    mid = (r + l)//2
    if isOk(mid, A, K):
        l = mid
    else:
        r = mid
print(l)
