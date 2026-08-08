N, K, R = input().split()
K, R = int(K), int(R)
M = [int(l) for l in N]
L = len(M)
MOD = 10 ** 9 + 7
if K == 1 and R == 0:
    M[-1] -= 2
    if M[-1] < 0:
        for i in range(L-1, 0, -1):
            if M[i] >= 0:
                break
            M[i] = 10 + M[i]
            M[i-1] -= 1
    result = 0
    for m in M:
        result = result * 10 + m
        result %= MOD
    print(result)
else:
    print(0)
