def isOk(N: int, M: int, K: int, data: list[int], mid: int)->bool:
    l = data[0]
    k = 1
    m = 0
    for i in range(N):
        m += 1
        if m > M or data[i] - l > mid:
            k += 1
            l = data[i]
            m = 1
            if k > K:
                return False
    return True

N, K, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
l = -1
r = max(A)
while r - l > 1:
    mid = (r + l) // 2
    if isOk(N, M, K, A, mid):
        r = mid
    else:
        l = mid
print(r)
