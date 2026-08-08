def calc(N: int, W: list[int], idx: int, S: int)->int:
    s = 0
    c = 0
    for i in range(idx, N):
        s += W[i]
        if s > S:
            return -1
        if s == S:
            s = 0
            c += 1
    return c + 1


N = int(input())
W = list(map(int, input().split()))
mx, mn = max(W), min(W)
sm = sum(W)
s = 0
result = 0
for i in range(N):
    s += W[i]
    if s < mx:
        continue
    if sm % s:
        continue
    if sm < s * 2:
        result = 1
        break
    r = calc(N, W, i+1, s)
    if r >= 1:
        result = r
        break
print(result)
