N, C = map(int, input().split())
W = list(map(int, input().split()))
weight = []
full = (1 << N) - 1
for i in range(1 << N):
    mask = i
    b = 1
    s = 0
    for j in range(N):
        if mask & b:
            s += W[j]
        b <<= 1
    weight.append(s)
# 運んだmask
dp = {0}
memo = [False] * (1 << N)
result = 0
while full not in dp:
    newDP = set()
    for mask in dp:
        if memo[mask]:
            continue
        memo[mask] = True
        remain = full ^ mask
        subRemain = remain
        while subRemain:
            s = weight[subRemain]
            if s <= C:
                newDP.add(mask | subRemain)
            subRemain = (subRemain - 1) & remain
    dp = newDP
    result += 1
    if full in dp:
        break
print(result)
