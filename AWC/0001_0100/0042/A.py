N, K = map(int, input().split())
result = 0
for n in range(N):
    a, b = map(int, input().split())
    c = a + b
    result += (a + b + K - 1)//K
print(result)
