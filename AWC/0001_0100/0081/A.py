N = int(input())
result = 0
for _ in range(N):
    t, s = input().split()
    result += t != s
print(result)
