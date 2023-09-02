def check(H, W, y, x, dy, dx, S):
    c = "snuke"
    for i in range(5):
        if y + dy * i < 0 or y + dy * i >= H:
            return False
        if x + dx * i < 0 or x + dx * i >= W:
            return False
        if S[y + dy * i][x + dx * i] != c[i]:
            return False
    return True


def calc(H, W, S):
    for h in range(H):
        for w in range(W):
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if not dy and not dx:
                        continue
                    if check(H, W, h, w, dy, dx, S):
                        return h, w, dy, dx
    return False


H, W = [int(l) for l in input().split()]
S = [input() for _ in range(H)]
h, w, dy, dx = calc(H, W, S)
for i in range(5):
    print(h + dy * i + 1, w + dx * i + 1)
