N, K = map(int, input().split())
S = list(map(int, input().split()))
data = []
for n in range(N):
    data.append((-S[n], n))
data.sort()
print(data[K-1][1] + 1)
