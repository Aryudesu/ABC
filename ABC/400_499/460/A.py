N, M = map(int, input().split())
result = 0
while M > 0:
    M = N % M
    result += 1
print(result)
