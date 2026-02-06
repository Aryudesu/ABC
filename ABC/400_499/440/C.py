def solve():
    N, W = map(int, input().split())
    C = list(map(int, input().split()))
    if W >= N:
        return 0
    data = [0] * (2*W)
    for i in range(N):
        data[i % (2*W)] += C[i]
    l = 0
    r = W-1
    s = 0
    for i in range(0, W):
        s += data[i]
    result = s
    for i in range(2*W):
        s -= data[l]
        l += 1
        r = (r + 1) % (2*W)
        s += data[r]
        result = min(result, s)
    return result

T = int(input())
for t in range(T):
    res = solve()
    print(res)
