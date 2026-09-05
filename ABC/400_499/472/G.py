from atcoder.dsu import DSU
from collections import defaultdict

def getPm1(c: str)->int:
    match c:
        case "+":
            return 1
        case "-":
            return -1
        case "#":
            return 0
        case _:
            raise ValueError()

def hw2num(H: int, W: int, h: int, w: int)->int:
    return W * h + w

H, W = map(int, input().split())
S = [input() for _ in range(H)]
sm = 0
for h in range(H):
    for w in range(W):
        sm += getPm1(S[h][w])

field = [[None] * W for _ in range(H)]
dsu = [DSU(W) for _ in range(H)]
for h in range(H):
    prev = None
    for w in range(W):
        if S[h][w] == "#":
            prev = None
            continue
        if prev is None:
            prev = getPm1(S[h][w])
            field[h][w] = prev
            continue
        prev += getPm1(S[h][w])
        field[h][w] = prev
    for w in range(W-1):
        if S[h][w] == "#" or S[h][w+1] == "#":
            continue
        dsu[h].merge(w, w + 1)
    prev = None
    for w in range(W-1, -1, -1):
        if S[h][w] == "#":
            prev = None
            continue
        if prev is None:
            prev = field[h][w]
            field[h][w] = prev
            continue
        field[h][w] = prev

result = 10 ** 18
roots = set()
graph = defaultdict(set)
for h in range(H-1, -1, -1):
    for w in range(W):
        if S[h][w] == "#":
            continue
        result = min(result, field[h][w])
        leader1 = dsu[h].leader(w)
        roots.add((h, leader1, field[h][w]))
        if h - 1 >= 0 and S[h-1][w] != "#":
            leader2 = dsu[h-1].leader(w)
            graph[(h, leader1, field[h][w])].add((h-1, leader2, field[h-1][w]))
data = dict()
while roots:
    nextRoots = set()
    for h, l, v in roots:
        for h2, l2, v2 in graph[(h, l, v)]:
            result = min(result, v + v2)
            nextRoots.add((h2, l2, v + v2))
    roots = nextRoots
print(sm - result)
