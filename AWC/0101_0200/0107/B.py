N, M, K = map(int, input().split())
data = [int(input()) for _ in range(N)]
for _ in range(M):
    data.append(int(input()))
data.sort()
result = 0
for k in range(K):
    result += data.pop()
print(result)
