H, W, X, Y = [int(l) for l in input().split()]
S = []
x = Y - 1
y = X - 1
for h in range(H):
    S.append(input())
result = 1
for dx in range(-1, 2):
    for dy in range(-1, 2):
        if dx == 0 and dy == 0:
            continue
        if dx * dy != 0:
            continue
        c = 1
        while True:
            t_x = x + dx * c
            t_y = y + dy * c
            # print(t_x, t_y)
            if t_x < 0 or t_x >= W or t_y < 0 or t_y >= H:
                break
            if S[t_y][t_x] == "#":
                break
            else:
                result += 1
            c += 1
print(result)
