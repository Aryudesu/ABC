N, M = map(int, input().split())
P = list(map(int, input().split()))
for m in range(M):
    u, v, w = map(int, input().split())
    P[u-1] -= w
    P[v-1] += w
result = 0
for i in range(N):
    if P[result] < P[i]:
        result = i
print(result + 1)
