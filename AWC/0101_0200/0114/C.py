from sortedcontainers import SortedSet

N, M = map(int, input().split())
data = SortedSet()
for n in range(N):
    x, c = map(int, input().split())
    data.add((x, c))
result = 0
for m in range(M):
    l, r = map(int, input().split())
    idx = data.bisect_right((l, 0))
    while data:
        if len(data) <= idx:
            break
        x, c = data[idx]
        if l <= x <= r:
            result += c
            data.pop(idx)
        else:
            break
print(result)
