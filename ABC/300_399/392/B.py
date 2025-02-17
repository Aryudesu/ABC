def calc(N, M, A):
    result = []
    for i in range(1, N + 1):
        if not i in A:
            result.append(i)
    return result

N, M = [int(l) for l in input().split()]
A = set([int(l) for l in input().split()])
res = calc(N, M, A)
print(len(res))
print(*res)
