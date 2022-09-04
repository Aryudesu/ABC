N, K = [int(l) for l in input().split()]
for k in range(K):
    N = (N * 1000 + 200) if N % 200 else N // 200
print(N)
