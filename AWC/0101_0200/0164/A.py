N = int(input())
result = 0
for _ in range(N-1):
    u, v, w = map(int, input().split())
    result += w
print(result)
