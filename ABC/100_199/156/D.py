N, A, B = map(int, input().split())
MOD = 10**9 + 7
result = pow(2, N, MOD)
num = 1
for n in range(max(A + 1, B + 1)):
    num = ((num * (N - n)) * pow(n + 1, MOD-2, MOD)) % MOD
    if n + 1 == A or n + 1 == B:
        result = (result - num) % MOD
print((result - 1) % MOD)
