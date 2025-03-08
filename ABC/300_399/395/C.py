def calc(N, A):
    Aset = set(A)
    if len(A) == len(Aset):
        return -1
    memo = dict()
    result = 10 ** 10
    for i in range(N):
        a = A[i]
        tmp = memo.get(a)
        if tmp is None:
            memo[a] = i
        else:
            r = i - tmp + 1
            result = min([r, result])
    return result

N = int(input())
A = [int(l) for l in input().split()]
result = calc(N, A)
print(result)
