def make_field(H, W):
    result = []
    for h in range(H + 1):
        result.append([0]*(W + 1))
    return result


H, W, N = [int(l) for l in input().split()]
field = make_field(H, W)
for n in range(N):
    A, B, C, D = [int(l) for l in input().split()]
    field[A][B] += 1
    if C + 1 < H and D + 1 < W:
        field[C + 1][D + 1] -= 1
print(field)
