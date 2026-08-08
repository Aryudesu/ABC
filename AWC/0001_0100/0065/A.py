N, K = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)
print(N//K + S - (1 if N % K == 0 else 0))
