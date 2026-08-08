N, D = map(int, input().split())
result = 0
for n in range(N):
    x, y = map(int, input().split())
    if x * x + y * y > D * D:
        result += 1
print(result)
