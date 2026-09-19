N = int(input())
result = 0
num = 0
for _ in range(N):
    a, b = map(int, input().split())
    c = a - b
    num += c
    result = min(result, num)
print(-result)
