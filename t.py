def calc(N, K):
    result = []
    memo = []
    for c in range(K):
        d = int((N + c**2) ** 0.5)
        for i in range(-1, 2):
            e = d + i
            if e ** 2 - c ** 2 == N:
                result.append((e, c))
                memo.append(((e + c), (e-c)))
    return result, memo


N = 4047
K = 1000000
print(calc(N, K))
