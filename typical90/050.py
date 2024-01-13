N, L = [int(l) for l in input().split()]
MOD = 10 ** 9 + 7
data = [0] * (N + 1)
data[0] = 1
for n in range(N):
    data[n + 1] = (data[n] + data[n + 1]) % MOD
    if n + L <= N:
        data[n + L] = (data[n] + data[n + L]) % MOD
print(data[-1])
