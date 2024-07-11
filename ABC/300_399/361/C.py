N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
A.sort()
# print(*A)
result = A[N - K - 1] - A[0]
# print(N - K - 1, 0, A[K] - A[0])
for idx in range(1, K + 1):
    s = A[idx + N - K - 1] - A[idx]
    # print(idx + N - K - 1, idx, s)
    if result > s:
        result = s
print(result)
