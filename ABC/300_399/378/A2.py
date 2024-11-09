m = dict()
S = set()
A = [int(l) for l in input().split()]
for a in A:
    m[a] = m.get(a, 0) + 1
    S.add(a)
result = 0
for s in S:
    if m[s] >= 2:
        result += 1
print(result)
