def calc(N, K, A):
    result = 0
    idx = 0
    count = 0
    while idx < N:
        count = 0
        count += A[idx]
        idx += 1
        while idx < N:
            if count + A[idx] <= K:
                count += A[idx]
                idx += 1
            else:
                break
        result += 1
    return result


N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
print(calc(N, K, A))
