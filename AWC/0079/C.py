INF = 10**18
N, Q = map(int, input().split())
AB = []
prev = 0
for n in range(N):
    a, b = map(int, input().split())
    AB.append((a - b) + prev)
    prev = AB[-1]

intervalDiffs = AB[-1]
minDiffs = min(AB)
for _ in range(Q):
    n, *query = list(map(int, input().split()))
    if n == 1:
        i, a, b = query
        now = AB[i - 1]
        for idx in range(i-1, N):
            AB[idx] += (a - b) - now
        minDiffs = min(AB)
        intervalDiffs = AB[-1]
    elif n == 2:
        d = query[0]
        if d + minDiffs <= 0:
            for i in range(N):
                if d + AB[i] <= 0:
                    print(i+1)
                    break
        else:
            pass
    else:
        raise ValueError()
