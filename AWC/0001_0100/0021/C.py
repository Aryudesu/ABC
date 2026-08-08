N, K = map(int, input().split())
result = 0
data = []
for n in range(N):
    c, m, *P = list(map(int, input().split()))
    P.sort(reverse=True)
    data.append(max(sum(P) - c, 0))
data.sort(reverse=True)
print(sum(data[:K]))
