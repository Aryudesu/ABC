def calc(N, A, base):
    memo = set()
    result = 0
    M = N // 2
    l = base
    r = base
    for l in range(base, N, 2):
        while (r + 1 < N) and (not A[r] in memo) and (A[r] == A[r + 1] and A[l] == A[l + 1]):
            memo.add(A[r])
            r += 2
        result = max([result, len(memo) * 2])
        # print(memo)
        if l == r:
            r += 2
        else:
            memo.discard(A[l])
        # print(l, r)
    return result

N = int(input())
A = [int(l) for l in input().split()]
res = calc(N, A, 0)
res = max([res, calc(N, A, 1)])
print(res)
