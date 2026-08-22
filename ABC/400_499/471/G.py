N, K, seed, M = map(int, input().split())
A = [None] * N
B = list(map(int, input().split()))
V = list(map(int, input().split()))
state = seed
MOD32 = 1 << 32
MOD64 = 1 << 64
for i in range(N):
    if i < M:
        A[i] = B[i]
    else:
        x = (((state >> 18) ^ state) >> 27) % MOD32
        r = state >> 59
        y = ((x >> r) + (x << (32 - r))) % MOD32
        A[i] = y % K
        state = (state * 6364136223846793005 + 2026081520260815) % MOD64

