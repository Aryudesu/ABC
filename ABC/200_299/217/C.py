N = int(input())
P = list(map(int, input().split()))
result = [None] * N
for i in range(N):
    result[P[i] - 1] = i + 1
print(*result)
