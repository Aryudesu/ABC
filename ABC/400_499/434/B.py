from collections import defaultdict
N, M = map(int, input().split())
data = defaultdict(list)
for n in range(N):
    a, b = map(int, input().split())
    data[a].append(b)
for m in range(M):
    print(sum(data[m+1])/len(data[m+1]))
