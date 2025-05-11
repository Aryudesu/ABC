H, W = [int(l) for l in input().split()]
S = []
for h in range(H):
    S.append(list(input()))
result = []
node = set()
for h in range(H):
    tmp = []
    for w in range(W):
        if S[h][w] == "E":
            node.add((h, w))
            tmp.append("E")
        elif S[h][w] == "#":
            tmp.append("#")
        else:
            tmp.append(None)
    result.append(tmp)
while node:
    new_node = set()
    for h, w in node:
        # 上
        if h - 1 >= 0:
            if S[h-1][w] == "." and result[h-1][w] is None:
                result[h-1][w] = "v"
                new_node.add((h-1, w))
        if h + 1 < H:
            if S[h+1][w] == "." and result[h+1][w] is None:
                result[h+1][w] = "^"
                new_node.add((h+1, w))
        if w - 1 >= 0:
            if S[h][w-1] == "." and result[h][w-1] is None:
                result[h][w-1] = ">"
                new_node.add((h, w-1))
        if w + 1 < W:
            if S[h][w+1] == "." and result[h][w+1] is None:
                result[h][w+1] = "<"
                new_node.add((h, w+1))
    node = new_node
for r in result:
    print("".join(r))
