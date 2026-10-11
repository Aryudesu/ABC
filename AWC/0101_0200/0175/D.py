def isOk(num: int, A: list[int], K: int)->bool:
    s = 0
    n = 0
    for a in A:
        s += a
        if s >= num:
            if a == num:
                s = 0
                n += 1
            else:
                if a > num:
                    return False
                s = a
            n += 1
    if s > 0:
        n += 1
    return n <= K


N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
mx = sum(A)
l = -1
r = mx + 1
while r - l > 1:
    mid = (r + l) // 2
    if isOk(mid, A, K):
        r = mid
    else:
        l = mid
print(r)
