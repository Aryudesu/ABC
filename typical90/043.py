from sortedcontainers import SortedSet


def calc(H, W, rs, cs, rt, ct, field):
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 回数 yの向き, xの向き, y, x
    data = [(0, -1, 0, rs, cs), (0, 1, 0, rs, cs), (0, 0, -1, rs, cs), (0, 0, 1, rs, cs)]
    sd = SortedSet(data)
    INF = H * W + 10
    memo = [[INF] * W for _ in range(H)]
    result = INF
    while data:
        c, dy, dx, y, x = sd.pop(0)
        if c >= result:
            break
        for i , j in dir:
            new_c = c
            if y + i >= H or y + i < 0 or x + j >= W or x + j < 0:
                continue
            if field[y+i][x+j] == "#":
                continue
            if i != dy or j != dx:
                new_c += 1
            if memo[y+i][x+j] < new_c:
                continue
            if new_c >= result:
                continue
            if y + i == rt and x + j == ct:
                result = min(result, new_c)
            else:
                sd.add((new_c, i, j, y + i, x + j))
    return result


H, W = [int(l) for l in input().split()]
rs, cs = [int(l) - 1 for l in input().split()]
rt, ct = [int(l) - 1 for l in input().split()]
field = []
for h in range(H):
    field.append(input())
print(calc(H, W, rs, cs, rt, ct, field))
