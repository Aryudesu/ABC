from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
# data[数字] = その数字の最長
data = defaultdict(int)
result = -1
for i in range(N):
    a = A[i]
    if data[a] < data[a-1] + 1:
        data[a] = data[a-1] + 1
        result = max(result, data[a])
print(result)
