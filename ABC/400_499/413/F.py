H, W, K = [int(l) for l in input().split()]
hall = set()
Field = [[0 for _ in range(W)] for _ in range(H)]
for k in range(K):
    r, c = [int(l) - 1 for l in input().split()]
    Field[r][c] = 1
    hall.add((r, c))

node = set()
for r, c in hall:
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j:
                continue
            if r + i < 0 or r + i >= H or c + j < 0 or c + j >= W:
                continue
            if (r + i, c + j) in hall:
                continue
            node.add((r + i, c + j))

print(node)

while node:
    new_node = set()
    move_flag = False
    for r, c in node:
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if r + i < 0 or r + i >= H or c + j < 0 or c + j >= W:
                    continue
                if Field[r + i][c + j] == 1:
                    count += 1
        if count >= 2:
            Field[r, c]
    node = new_node
