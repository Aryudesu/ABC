N, M = map(int, input().split())
data = [0] * N
for m in range(M):
    u, v = map(int, input().split())
    data[u-1] += v
    data[v-1] += u
print(max(data))
