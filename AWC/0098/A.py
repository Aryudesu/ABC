N, D = map(int, input().split())
T = list(map(int, input().split()))
result = [0] * N
for n in range(N):
    A = list(map(int, input().split()))
    for d in range(D):
        result[n] += abs(A[d] - T[n])
print(max(result))

