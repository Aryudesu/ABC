def check(N, K, A, B):
    D = [A[0], B[0]]
    for n in range(1, N):
        tmp = [-1, -1]
        if D[0] != -1:
            if abs(D[0] - A[n]) <= K:
                tmp[0] = A[n]
            if abs(D[0] - B[n]) <= K:
                tmp[1] = B[n]
        if D[1] != -1:
            if abs(D[1] - A[n]) <= K:
                tmp[0] = A[n]
            if abs(D[1] - B[n]) <= K:
                tmp[1] = B[n]
        if tmp[0] == -1 and tmp[1] == -1:
            return "No"
        D = tmp
    return "Yes"


N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
print(check(N, K, A, B))
