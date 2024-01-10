MOD = 10**9 + 7
K = int(input())
if K % 9 == 0:
    data = [0 for _ in range(K + 1)]
    data[0] = 1
    for k in range(K + 1):
        for i in range(1, 10):
            idx = k - i
            if idx >= 0:
                data[k] = (data[idx] + data[k]) % MOD
    print(data[K])
else:
    print(0)