from collections import defaultdict

dist = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def calc(H: int, W: int, dust: set, takaY: int, takaX: int, memo: dict) -> int|None:
    for dy, dx in dist:
        newDust = set()
        field = ""
        for dusty, dustx in dust:
            dusty += dy
            dustx += dx



H, W = [int(l) for l in input().split()]
S = []
for h in range(H):
    S.append("." * (W * 3))
for h in range(H):
    S.append("." * W + input() + "." * W)
for h in range(H):
    S.append("." * (W * 3))
field = "".join(S)
# その手になった盤面の最小手数（探索時）
memo = defaultdict(int)
memo[field] = 0
dust = set()
takaH = 0
takaW = 0
for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            dust.add((h, w))
            takaH = h
            takaW = w
for s in S:
    print(s)
