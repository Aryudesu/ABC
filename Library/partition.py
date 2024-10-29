def get2num(num: int, N: int) -> list:
    tmp = num
    result = []
    for _ in range(N):
        result.append(tmp % 2)
        tmp //= 2
    return result


def calc_coeff(A: list) -> dict:
    lA = len(A)
    result = dict()
    for i in range(1, 2 ** lA):
        tmp = get2num(i, lA)
        n = 0
        c = 0
        for i in range(lA):
            if tmp[i]:
                n += A[i]
                c += 1
        if c % 2:
            result[n] = result.get(n, 0) + 1
        else:
            result[n] = result.get(n, 0) - 1
    return result


def calc_partition(A, N):
    coeff = calc_coeff(A)
    keys = list(coeff.keys())
    keys.sort()
    result = [1]
    for i in range(1, N + 1):
        n = 0
        for k in keys:
            idx = i - k
            if idx < 0:
                break
            n += result[idx] * coeff.get(k, 0)
        result.append(n)
    return result


def calc_partition2(A, M):
    result = [0] * (M + 1)
    result[0] = 1
    lA = len(A)
    for i in range(lA):
        for j in range(A[i], M + 1):
            result[j] += result[j - A[i]]
    return result


M = int(input())
A = list(set([int(l) for l in input().split()]))
A.sort()
res1 = calc_partition(A, M)
res2 = calc_partition2(A, M)
for idx in range(len(res1)):
    print(idx, res1[idx], res2[idx])
