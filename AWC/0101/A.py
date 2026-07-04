N, M = map(int, input().split())
S = list(map(int, input().split()))
T = [0] * N
for m in range(M):
    u, v, w = map(int, input().split())
    T[u-1] += w
    T[v-1] += w
result = 0
for s, t in zip(S, T):
    result += t < s
print(result)
