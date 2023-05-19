def is_eq(A, B, dy, dx, H, W):
    for y in range(H):
        for x in range(W):
            if A[(dy + y) % H][(dx + x) % W] != B[y][x]:
                return False
    return True


def calc(A, B, H, W):
    for y in range(H):
        for x in range(W):
            if is_eq(A, B, y, x, H, W):
                return True
    return False


H, W = [int(l) for l in input().split()]
A = [input() for l in range(H)]
B = [input() for l in range(H)]
print("Yes" if calc(A, B, H, W) else "No")
