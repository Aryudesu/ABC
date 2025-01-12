from itertools import combinations

N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
if N== K:
    AXOR = A[0]
    for i in range(1, N):
        AXOR = AXOR ^ A[i]
    print(AXOR)
elif N // 2 > K:
    result = 0
    for data in combinations(A, K):
        tmp = data[0]
        for i in range(1, K):
            tmp = tmp^data[i]
        result = max([result, tmp])
    print(result)
else:
    AXOR = A[0]
    for i in range(1, N):
        AXOR = AXOR ^ A[i]
    if N == K:
        print(AXOR)
    result = 0
    for data in combinations(A, N - K):
        tmp = data[0]
        for i in range(1, N - K):
            tmp = tmp ^ data[i]
        result = max([result, AXOR ^ tmp])
    print(result)
