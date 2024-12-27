import heapq


def heap_update(H, W, y, x, X, S, data, memo):
    f = False
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dy != 0 and dx != 0:
                continue
            if dy == 0 and dx == 0:
                continue
            if y + dy < 0 or y + dy >= H:
                continue
            if x + dx < 0 or x + dx >= W:
                continue
            tmp = tuple([y + dy, x + dx])
            if tmp in memo:
                continue
            heapq.heappush(data, [S[y + dy][x + dx], tmp])
            memo.add(tmp)
            f = True
    return f


H, W, X = [int(l) for l in input().split()]
P, Q = [int(l) - 1 for l in input().split()]
S = []
for h in range(H):
    S.append([int(l) for l in input().split()])
cell_list = []
memo = set()
hp = S[P][Q]
memo.add(tuple([P, Q]))
heap_update(H, W, P, Q, X, S, cell_list, memo)
while True:
    if len(cell_list) == 0:
        break
    num, pos = heapq.heappop(cell_list)
    if num * X >= hp:
        break
    y, x = pos
    hp += num
    res = heap_update(H, W, y, x, X, S, cell_list, memo)
print(hp)
