import bisect


def calc(N, K, A):
    mx = A[0] * K
    data = [0]
    dset = set()
    count = 0
    dc = 1
    while count < K:
        for n in range(N):
            num = data[count] + A[n]
            if mx < num or (dc > K and data[K] < num):
                if n:
                    break
                else:
                    return data[K]
            if not num in dset:
                bisect.insort(data, num)
                dset.add(num)
                dc += 1
        count += 1
    return data[K]


N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
A.sort()
print(calc(N, K, A))
