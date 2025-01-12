def calc(N, K, A):
    p = 0
    count = 0
    data = [-1] * N
    while True:
        count += 1
        p = A[p]
        if count == K:
            return p + 1
        if data[p] != -1:
            if (K - count) % (count - data[p]) == 0:
                return p + 1
        data[p] = count

N, K = [int(l) for l in input().split()]
A = [int(l) - 1 for l in input().split()]
print(calc(N, K, A))
