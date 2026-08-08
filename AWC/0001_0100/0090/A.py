N = int(input())
result = 0
for n in range(N):
    a, b = map(int, input().split())
    result += max(0, a - b)
print(result)
