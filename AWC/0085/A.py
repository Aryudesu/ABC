N = int(input())
S = list(map(int, input().split()))
data = list(range(N))
result = [0] * N
c = 1
while len(data) > 1:
    nextData = []
    M = len(data)
    for i in range(M//2):
        if S[data[2*i]] < S[data[2*i + 1]]:
            result[data[2*i]] = c
            nextData.append(data[2*i + 1])
        else:
            result[data[2*i+1]] = c
            nextData.append(data[2*i])
    c += 1
    data = nextData
print(*result)
