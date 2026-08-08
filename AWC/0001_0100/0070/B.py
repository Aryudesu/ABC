N = int(input())
A = list(map(int, input().split()))
result = 0
kMk = 0
for n in range(N):
    kMk += A[n]
    if (n + 1) * A[n] >= kMk:
        result += 1
print(result)
