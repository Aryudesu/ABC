def calc(A, W, N):
    res = []
    for i in range(N):
        if A[i] <= W:
            res.append(A[i])
            for j in range(N):
                if i == j:
                    continue
                if A[i] + A[j] <= W:
                    res.append(A[i] + A[j])
                    for k in range(N):
                        if A[i] + A[j] + A[k] <= W:
                            if j == k or i == k:
                                continue
                            res.append(A[i] + A[j] + A[k])
    print(len(set(res)))


N, W = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
calc(A, W, N)
