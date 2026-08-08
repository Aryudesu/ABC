from sortedcontainers import SortedList

N, Q = map(int, input().split())
D = list(map(int, input().split()))
data = SortedList()
for idx in range(N):
    data.add((idx, D[idx]))
result = []
for _ in range(Q):
    t = int(input())
    idx = t - 1
    if idx >= len(data):
        result.append(len(data))
        continue
    index, d = data.pop(idx)
    if d == 1:
        result.append(len(data))
        continue
    data.add((index, d - 1))
    result.append(len(data))
for r in result:
    print(r)
