N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = set(map(int, input().split()))
data = []
for i in range(N):
    if (i + 1) in B and A[i] < K:
        data.append(A[i])
print(len(data), sum(data))
