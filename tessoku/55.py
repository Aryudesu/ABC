from sortedcontainers import SortedSet

Q = int(input())
data = SortedSet()
for _ in range(Q):
    n, x = [int(l) for l in input().split()]
    if n == 1:
        data.add(x)
    elif n == 2:
        data.discard(x)
    elif n == 3:
        idx = data.bisect_left(x)
        print(-1 if idx >= len(data) else data[idx])
