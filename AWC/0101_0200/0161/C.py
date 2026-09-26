from collections import defaultdict

N, K = map(int, input().split())
T = list(map(int, input().split()))
dup = 0
data = defaultdict(int)
l = 0
shurui = 0
result = 0
for r in range(N):
    rt = T[r]
    data[rt] += 1
    if data[rt] > 1:
        dup += 1
    if data[rt] == 1:
        shurui += 1
    while dup > K:
        lt = T[l]
        data[lt] -= 1
        if data[lt] >= 1:
            dup -= 1
        if data[lt] == 0:
            shurui -= 1
        l += 1
    result = max(shurui, result)
print(result)
