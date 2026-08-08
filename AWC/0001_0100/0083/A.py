N, D = map(int, input().split())
result = 0
for i in range(N):
    a, b = map(int, input().split())
    result += a + b * D
print(result)
