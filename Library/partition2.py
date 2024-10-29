def calc_partition(A, M):
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
res = calc_partition(A, M)
print(res[-1])
