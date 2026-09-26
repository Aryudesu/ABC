from sortedcontainers import SortedList
N = int(input())
A = list(map(int, input().split()))
data = SortedList()
data.add(A[0])
data.add(A[1])
result = []
for idx in range(2, N):
    data.add(A[idx])
    result.append(data[-3])
print(*result, sep="\n")
