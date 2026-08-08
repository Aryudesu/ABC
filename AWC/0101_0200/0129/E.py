from sortedcontainers import SortedList

N = int(input())
A = list(map(int, input().split()))
A.reverse()
data = SortedList()
result = [0] * N
K = 0
for idx in range(N):
    a = A[idx]
    i = data.bisect_right((a, N))
    if i == 0:
        data.add((a, N-idx))
        result[N-idx-1] = 0
        K += 1
        continue
    b, j = data[i - 1]
    data.discard((b, j))
    data.add((a, N-idx))
    result[j-1] = N-idx
print(K)
print(*result)
