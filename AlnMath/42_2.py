N = int(input())
result = 0
for i in range(1, N + 1):
    M = N // i
    result += (i * M * (M + 1)) // 2
print(result)
