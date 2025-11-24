from collections import defaultdict

N, Q = map(int, input().split())
A = list(map(int, input().split()))
data = defaultdict(list)
for idx in range(N):
    a = A[idx]
    data[a].append(idx)
result = []
for q in range(Q):
    x, k = map(int, input().split())
    if len(data[x]) < k:
        result.append(-1)
        continue
    result.append(data[x][k-1]+1)
for r in result:
    print(r)
