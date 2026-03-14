from sortedcontainers import SortedList

N, Q = map(int, input().split())
D = list(map(int, input().split()))
data = SortedList(idx for idx in range(N))
result = []
for _ in range(Q):
    t = int(input()) - 1
    if t < len(data):
        idx = data[t]
        D[idx] -= 1
        if not D[idx]:
            data.discard(idx)
    result.append(len(data))
for r in result:
    print(r)
