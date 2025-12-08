from sortedcontainers import SortedSet

N, K = map(int, input().split())
X = list(map(int, input().split()))
data = SortedSet()

for i in range(K-1):
    data.add((X[i], i+1))
for i in range(K-1, N):
    data.add((X[i], i+1))
    print(data[K-1][1])
    # print(data)
