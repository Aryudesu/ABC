H, W, M = [int(l) for l in input().split()]
TAX = []
for m in range(M):
    TAX.append([int(l) for l in input().split()])
TAX.reverse()
col = set()
row = set()
result = dict()
for t, a, x in TAX:
    if t == 1:
        if not a in row:
            result[x] = result.get(x, 0) + (W - len(col))
            row.add(a)
    else:
        if not a in col:
            result[x] = result.get(x, 0) + (H - len(row))
            col.add(a)
palette = list(result.keys())
palette.sort()
res = []
all = 0
for p in palette:
    if p == 0:
        continue
    tmp = result.get(p, 0)
    if tmp > 0:
        tmp2 = (p, tmp)
        all += tmp
        res.append(tmp2)
NUM = len(res)
if H * W - all > 0:
    NUM += 1
print(NUM)
if H * W - all > 0:
    print(0, H * W - all)
for r in res:
    print(*r)
