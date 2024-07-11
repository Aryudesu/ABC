N = int(input())
A = [int(l) for l in input().split()]
W = [int(l) for l in input().split()]
data = [(A[i], W[i]) for i in range(N)]
data.sort()
numData = dict()

for dat in data:
    numData[dat[0]] = numData.get(dat[0], 0) + 1
result = 0
for n in range(N):
    a, w = data[n]
    if numData.get(a, 0) > 1:
        numData[a] = numData.get(a, 0) - 1
        result += w
print(result)
