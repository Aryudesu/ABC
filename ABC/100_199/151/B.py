N, K, M = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)
AM = N * M
if AM - S > K:
    print(-1)
else:
    print(max(AM - S, 0))
