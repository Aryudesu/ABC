N, M = map(int, input().split())
data = [0] * (N + 1)
dataC = [0] * (N + 1)
for n in range(N):
    c, k = map(int, input().split())
    data[n+1] = k
    dataC[n+1] = c
result = 0
for m in range(M):
    p = int(input())
    if data[p] > 0:
        result += dataC[p]
        data[p]-=1
print(result)
