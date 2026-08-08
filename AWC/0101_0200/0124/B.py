N, K = map(int, input().split())
data = []
for n in range(N):
    a, b = map(int, input().split())
    data.append((-a-b, n+1))
data.sort()
result = [i for s, i in data[:K]]
result.sort()
print(*result, sep="\n")
