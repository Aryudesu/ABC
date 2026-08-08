N = int(input())
A = list(map(int, input().split()))
data = A[:]
data.sort(reverse=True)
hightData = dict()
while data:
    a = data.pop()
    if len(data) == 0 or data[-1] != a:
        hightData[a] = len(data)
result = []
for idx in range(N):
    result.append(hightData[A[idx]])
print(*result)
