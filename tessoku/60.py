from collections import deque

N = int(input())
A = list(map(int, input().split()))
result = []
data = deque()
for i in range(N):
    while len(data) > 0 and data[0][0] <= A[i]:
        data.popleft()
    if len(data) == 0:
        result.append(-1)
    else:
        n, idx = data[0]
        result.append(idx + 1)
    data.appendleft((A[i], i))
print(*result)
