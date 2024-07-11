def calc(N, M, A, B):
    C = A + B
    C.sort()
    Adata = set(A)
    data = C[0] in Adata
    for idx in range(1, N + M):
        if C[idx] in Adata:
            if data:
                return True
            data = True
        else:
            data = False
    return False


N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
print("Yes" if calc(N, M, A, B) else "No")
