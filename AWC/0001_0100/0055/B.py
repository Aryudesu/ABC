N, P, Q= map(int, input().split())
pos = []
for n in range(N):
    x, c = map(int, input().split())
    pos.append((x, c))
pos.sort()
pPos = 0
qPos = 0
for idx in range(N):
    x, c = pos[idx]
    if abs(x - P) < abs(pos[pPos][0] - P):
        pPos = idx
    if abs(x - Q) < abs(pos[qPos][0] - Q):
        qPos = idx
pData = {pPos, qPos}
result = 0
for p in pData:
    result += pos[p][1] + (1 if len(pData) == 2 else 2)
print(result)
