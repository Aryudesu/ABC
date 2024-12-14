H, W, D = [int(l) for l in input().split()]
S = []
pos = set()
result = set()
for h in range(H):
    s = input()
    for w in range(W):
        if s[w] == "H":
            tmp = tuple([h, w])
            pos.add(tmp)
            result.add(tmp)
    S.append(s)
for d in range(D):
    if len(pos) == 0:
        break
    new_pos = set()
    for y, x in pos:
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
                if S[y + dy][x + dx] == "#":
                    continue
                np = tuple([y + dy, x + dx])
                if np in result:
                    continue
                result.add(np)
                new_pos.add(np)
    pos = new_pos
# print(result)
print(len(result))
