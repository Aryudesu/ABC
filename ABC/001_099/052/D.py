N, A, B = map(int, input().split())
X = list(map(int, input().split()))
result = 0
for i in range(N-1):
    tmp1 = A * (X[i+1] - X[i])
    result += min(tmp1, B)
print(result)
