N = int(input())
result = 0
for n in range(N):
    a, t = map(int, input().split())
    result += a * t
print(result)
