H, W = [int(l) for l in input().split()]
Field = []
person = set()
S = None
G = None
for h in range(H):
    tmp = list(input())
    for w in range(W):
        if tmp[w] == ">" or tmp[w] == "<" or tmp[w] == "v" or tmp[w] == "^":
            person.add((h, w, tmp[w]))
        elif tmp[w] == "S":
            S = (h, w)
        elif tmp[w] == "G":
            G = (h, w)
    Field.append(tmp)
for p in person:
    h = p[0]
    w = p[1]
    v = p[2]
    if v == ">":
        w += 1
        while w < W:
            if Field[h][w] != "." and Field[h][w] != "*":
                break
            Field[h][w] = "*"
            w += 1
    elif v == "<":
        w -= 1
        while w >= 0:
            if Field[h][w] != "." and Field[h][w] != "*":
                break
            Field[h][w] = "*"
            w -= 1
    elif v == "^":
        h -= 1
        while h >= 0:
            if Field[h][w] != "." and Field[h][w] != "*":
                break
            Field[h][w] = "*"
            h -= 1
    elif v == "v":
        h += 1
        while h < H:
            if Field[h][w] != "." and Field[h][w] != "*":
                break
            Field[h][w] = "*"
            h += 1
# for f in Field:
#     print(f)

result = 0
node = set()
node.add(S)
goal = False
while True:
    result += 1
    new_node = set()
    for p in node:
        h, w = p
        if h-1 >= 0:
            if Field[h - 1][w] == ".":
                new_node.add((h - 1, w))
            elif Field[h - 1][w] == "G":
                goal = True
        if h + 1 < H:
            if Field[h + 1][w] == ".":
                new_node.add((h + 1, w))
            elif Field[h][w] == "G":
                goal = True
        if w - 1 >= 0:
            if Field[h][w - 1] == ".":
                new_node.add((h, w - 1))
            elif Field[h][w - 1] == "G":
                goal = True
        if w + 1 < W:
            if Field[h][w + 1] == ".":
                new_node.add((h, w + 1))
            elif Field[h][w + 1] == "G":
                goal = True
        if goal:
            break
        Field[h][w] = "#"
    if goal:
        break
    node = new_node
    # print(node)
    if not len(new_node):
        result = -1
        break
print(result)
