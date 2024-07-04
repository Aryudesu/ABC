def divM(N, M=10):
    while N % M == 0:
        N //= M
    return N % 10


def calc(N):
    result = 1
    for i in range(1, N + 1):
        if (i % 10) == 2 and (i % 10) == 5:
            result = (result * (i % 10)) % 10
    return result

N = calc(int(input()))
print(N)
