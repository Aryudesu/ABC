MOD = 10 ** 9
N, K = [int(l) for l in input().split()]
result = 0
num = []
data = []
for i in range(N + 1):
    if 0 <= i and i < K:
        num.append(1)
        data.append(i + 1)
    elif i == K:
        num.append(K)
        data.append((data[-1] + K) % MOD)
    else:
        num.append((data[i - 1] - data[i - K - 1]) % MOD)
        data.append((data[i-1] + num[-1]) % MOD)
print(num[-1])
