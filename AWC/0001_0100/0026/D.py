from collections import defaultdict

N, K = map(int, input().split())
data = defaultdict(int)
pos = set()
for n in range(N):
    l, r = map(int, input().split())
    l = l
    r = r
    data[l] += 1
    data[r] -= 1
    pos.add(l)
    pos.add(r)
pos = sorted(pos)
imos = []
s = 0
for p in pos:
    s += data[p]
    imos.append(s)
rge = []
l = -1
isRge = False
for idx in range(len(pos)):
    p = pos[idx]
    if imos[idx] >= K and not isRge:
        l = p
        isRge = True
    elif imos[idx] < K and isRge:
        rge.append((l, p))
        isRge = False
result = 0
for l, r in rge:
    result += r-l
print(result)
