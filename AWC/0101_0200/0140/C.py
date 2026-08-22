N, K = map(int, input().split())
A = list(map(int, input().split()))
INF = 10 ** 18
uke = [-INF] * N
ukenai = [-INF] * N
uke[0] = A[0]
ukenai[0] = 0
for i in range(1, N):
    uke[i] = max(ukenai[i-1] + A[i], uke[i-1] + A[i] - K)
    ukenai[i] = max(uke[i-1], ukenai[i-1])
print(max(max(uke), max(ukenai)))
