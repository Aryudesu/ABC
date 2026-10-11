N, M = map(int, input().split())
W = list(map(int, input().split()))
result = [False] * N
for _ in range(M):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    if W[u] < W[v]:
        result[u] = True
    elif W[u] > W[v]:
        result[v] = True
print(sum(result))
