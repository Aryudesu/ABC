def calc(N, M):
    m = M
    m_max = N * N
    while True:
        if m > m_max:
            return -1
        T = int(m ** 0.5)
        for i in range(T, 0, -1):
            if m % i == 0:
                if m // i <= N:
                    return m
                else:
                    break
            elif m // i > N:
                break
        m += 1


N, M = [int(l) for l in input().split()]
print(calc(N, M))
