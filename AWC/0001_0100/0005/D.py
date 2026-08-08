def isOk(A, mid, N, K):
    s = 0
    c = 0
    for a in A:
        s += a
        if s >= mid:
            s = 0
            # トラック1つ
            c += 1
            if c == K:
                return True
    return False

N, K = map(int, input().split())
A = list(map(int, input().split()))
M = sum(A)
l = 0 - 1
r = M + 1
while r - l > 1:
    m = (r + l) // 2
    if isOk(A, m, N, K):
        l = m
    else:
        r = m
print(l)
