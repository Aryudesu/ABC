N = int(input())
X = list(map(int, input().split()))
X.sort()
result = 0
for i in range(N):
    result += abs(X[i] - X[(i+1)%N])
print(result)
