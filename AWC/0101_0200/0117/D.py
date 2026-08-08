from sortedcontainers import SortedList

N, M = map(int, input().split())
DV = []
for _ in range(N):
    d, v = map(int, input().split())
    DV.append((v, d))
DV.sort(reverse=True)
L = SortedList(map(int, input().split()))
result = 0
for v, d in DV:
    if not L:
        break
    idx = L.bisect_left(d)
    if idx >= len(L):
        continue
    L.pop(idx)
    result += v
print(result)
