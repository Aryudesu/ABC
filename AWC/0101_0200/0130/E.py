from sortedcontainers import SortedList

N, K, D = map(int, input().split())
H = list(map(int, input().split()))
data = SortedList(H[:K])
result = H.copy()
m = data[0]
for k in range(K):
    result[k] = min(m + D)
