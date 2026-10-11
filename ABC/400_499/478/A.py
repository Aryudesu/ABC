N, M = map(int, input().split())
result = [M//N] * N
for i in range(M%N):
    result[i] += 1
print(*result, sep="\n")
