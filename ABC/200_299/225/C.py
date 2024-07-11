def calc(N, M, B):
    base = B[0][0]
    if ((base - 1) % 7) + M > 7:
        return False
    for x in range(M):
        for y in range(N):
            if y * 7 + x != B[y][x] - base:
                return False
    return True


N, M = [int(l) for l in input().split()]
B = []
for n in range(N):
    B.append([int(l) for l in input().split()])
print("Yes" if calc(N, M, B) else "No")
