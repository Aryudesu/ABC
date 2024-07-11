def calc(N, M, H):
    tmpM = M
    for idx in range(N):
        h = H[idx]
        tmpM -= h
        if tmpM < 0:
            return idx
        elif tmpM == 0:
            return idx + 1
    return N

N, M = [int(l) for l in input().split()]
H = [int(l) for l in input().split()]
print(calc(N, M, H))
