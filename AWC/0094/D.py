MOD = 10**9 + 7
N, A, B, C = map(int, input().split())
M = A * B * C
numer = 1
for i in range(1, N + 1):
    numer = (numer * (M - i + 1)) % MOD
print(numer)
