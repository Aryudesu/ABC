N, T = map(int, input().split())
result = 0
for n in range(N):
    a, b = map(int, input().split())
    result += max(a - b * T, 0)
print(result)
