INF = 2000
def isOk(A: list[int], mid: int, K: int)->bool:
    print("debug")
    MA = A[0]
    MI = A[0]
    k = 0
    for a in A:
        ma = max(MA, a)
        mi = min(MI, a)
        if ma - mi > mid:
            k += 1
            MA = a
            MI = a
        else:
            MA = ma
            MI = mi
        print(MA, MI, k, mid)
    return k + 1 <= K


N, K = map(int, input().split())
A = list(map(int, input().split()))
M = 1000
r = M + 1
l = -1
while r - l > 1:
    mid = (r + l) // 2
    if isOk(A, mid, K):
        r = mid
    else:
        l = mid
print(r)
