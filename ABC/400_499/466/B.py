N, M = map(int, input().split())
result = [-1] * M
for n in range(N):
    c, s = map(int, input().split())
    result[c-1] = max(result[c-1], s)
print(*result)
