def calc(H, W, A):
    for i1 in range(H - 1):
        for i2 in range(i1 + 1, H):
            for j1 in range(W - 1):
                for j2 in range(j1 + 1, W):
                    if A[i1][j1] + A[i2][j2] > A[i2][j1] + A[i1][j2]:
                        return False
    return True

H, W = [int(l) for l in input().split()]
A = []
for h in range(H):
    A.append([int(l) for l in input().split()])
print("Yes" if calc(H, W, A) else "No")
