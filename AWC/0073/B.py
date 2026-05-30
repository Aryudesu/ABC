N, K = map(int, input().split())
allFSum = 0
data = []
for n in range(N):
    f, b = map(int, input().split())
    data.append(b-f)
    allFSum += f
data.sort(reverse=True)
print(allFSum + sum(data[:K]))
