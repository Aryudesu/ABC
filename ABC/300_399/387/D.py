H, W = [int(l) for l in input().split()]
S = []
# [h, w, 向き: 0:前の動きが横 1:前の動きが縦]
nodes = set()
goal_w = None
goal_h = None
for h in range(H):
    s = input()
    for w in range(W):
        if s[w] == "S":
            tmp = tuple([h, w, 0])
            nodes.add(tmp)
            tmp = tuple([h, w, 1])
            nodes.add(tmp)
        elif s[w] == "G":
            goal_w = tuple([h, w, 0])
            goal_h = tuple([h, w, 1])
    S.append(s)
result = 0
goal_f = False
memo = set()
while nodes:
    new_nodes = set()
    result += 1
    for h, w, d in nodes:
        if d == 0:
            if h + 1 < H and S[h + 1][w] != "#":
                tmp = tuple([h + 1, w, 1])
                if not tmp in memo:
                    new_nodes.add(tmp)
                    memo.add(tmp)
            if h - 1 >= 0 and S[h - 1][w] != "#":
                tmp = tuple([h - 1, w, 1])
                if not tmp in memo:
                    new_nodes.add(tmp)
                    memo.add(tmp)
        if d == 1:
            if w + 1 < W and S[h][w + 1] != "#":
                tmp = tuple([h, w + 1, 0])
                if not tmp in memo:
                    new_nodes.add(tmp)
                    memo.add(tmp)
            if w - 1 >= 0 and S[h][w - 1] != "#":
                tmp = tuple([h, w - 1, 0])
                if not tmp in memo:
                    new_nodes.add(tmp)
                    memo.add(tmp)
    if goal_h in new_nodes or goal_w in new_nodes:
        goal_f = True
        break
    nodes = new_nodes
print(result if goal_f else -1)
