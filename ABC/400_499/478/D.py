from collections import defaultdict
N, Q = map(int, input().split())
imos = defaultdict(list)
for _ in range(Q):
    l, r, x = map(int, input().split())
    imos[l-1].append(x)
    imos[r].append(-x)
result = []
counter = defaultdict(int)
data = set()
for i in range(N):
    if i in imos:
        dat = imos[i]
        for d in dat:
            if d > 0:
                counter[d] += 1
            else:
                counter[-d] -= 1
        for d in dat:
            if counter[abs(d)] > 0:
                data.add(abs(d))
            else:
                data.discard(abs(d))
    result.append(len(data))
print(*result)
