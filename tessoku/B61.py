from collections import defaultdict
N, M = map(int, input().split())
data = [0] * N
for m in range(M):
    a, b = map(int, input().split())
    data[a-1] += 1
    data[b-1] += 1
res = 0
for i in range(N):
    if data[res] < data[i]:
        res = i
print(res+1)
