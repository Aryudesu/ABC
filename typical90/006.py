N, K = [int(l) for l in input().split()]
S = input()
data = []
for i in range(N):
    data.append((S[i], i))
data.sort()
print(data)
