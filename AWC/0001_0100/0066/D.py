# K以下にできるか
def isOk(S: int, A: list[int], mid: int, K: int)->int:
    k = 1
    s = 0
    for a in A:
        s += a
        S -= a
        if s > mid:
            s = a
            if s > mid:
                return False
            k += 1
            if k > K:
                return False
    return k <= K and S + s <= mid

N, K = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)
l = -1
r = S + 1
while r - l > 1:
    mid = (r + l) // 2
    if isOk(S, A, mid, K):
        r = mid
    else:
        l = mid
print(r)
