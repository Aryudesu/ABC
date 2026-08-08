N, K = map(int, input().split())
data = []
for n in range(N):
    t, c = map(int, input().split())
    data.append(t + c)
data.sort(reverse=True)
print(sum(data[:K]))
