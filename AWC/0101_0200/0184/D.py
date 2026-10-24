def calc(N: int, mask: int, W: int, H: list[int])->int:
    imos = [0] * (N + 1)
    for n in range(N):
        b = 1 << n
        if mask & b:
            imos[max(1, (n + 1) - (W-1)//2) - 1] += 1
            imos[min(N, (n + 1) + W//2)] -= 1
    result = 0
    s = 0
    for n in range(N):
        s += imos[n]
        if not s:
            result += H[n]
    return result


N, W, K = map(int, input().split())
H = list(map(int, input().split()))
result = sum(H)
for mask in range(1 << N):
    if mask.bit_count() > K:
        continue
    res = calc(N, mask, W, H)
    result = min(result, res)
print(result)
