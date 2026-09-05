N, K, M = map(int, input().split())
S = list(map(int, input().split()))
D = []
if M > 0:
    D = list(map(int, input().split()))
INF = 10 ** 18
data = []
for n in range(N):
    data.append((-S[n], n))
for d in D:
    data[d-1] = (INF, INF)
data.sort()
isOk = False
for k in range(K):
    if data[k][1] == 0:
        isOk = True
        break
print("Yes" if isOk else "No")
