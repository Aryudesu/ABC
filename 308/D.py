snuke = "snuke"


def calc(H, W, S):
    count = 1
    if S[0][0] != "s":
        return False
    F = []
    for _ in range(H):
        tmp = []
        for _ in range(W):
            tmp.append(False)
        F.append(tmp)
    node = set()
    node.add((0, 0))
    while node:
        new_node = set()
        for nd in node:
            x, y = nd
            if x == W - 1 and y == H - 1:
                return True
            if x + 1 < W:
                if not F[y][x + 1] and snuke[count] == S[y][x + 1]:
                    F[y][x + 1] = True
                    new_node.add((x + 1, y))
            if x - 1 >= 0:
                if not F[y][x - 1] and snuke[count] == S[y][x - 1]:
                    F[y][x - 1] = True
                    new_node.add((x - 1, y))
            if y + 1 < H:
                if not F[y + 1][x] and snuke[count] == S[y + 1][x]:
                    F[y + 1][x] = True
                    new_node.add((x, y + 1))
            if y - 1 >= 0:
                if not F[y - 1][x] and snuke[count] == S[y - 1][x]:
                    F[y - 1][x] = True
                    new_node.add((x, y-1))
        count = (count + 1) % 5
        node = new_node


H, W = [int(l) for l in input().split()]
S = []
for h in range(H):
    S.append(input())
print("Yes" if calc(H, W, S) else "No")
