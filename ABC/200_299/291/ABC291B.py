N = int(input())
X = [int(l) for l in input().split()]
X.sort()
result = 0
for i in range(N, 4*N):
    result += X[i]
print(result/(3*N))
