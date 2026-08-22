from collections import defaultdict
from typing import Tuple

def calcData(H: int, W: int, G: list[str], initR: int, initC: int, S: str)->list[Tuple[int, int]]:
    r = initR
    c = initC
    result = [(r + 1, c + 1)]
    for s in S:
        if s == "L":
            if c - 1 >= 0 and G[r][c - 1] != "#":
                c = c - 1
        elif s == "R":
            if c + 1  < W and G[r][c + 1] != "#":
                c = c + 1
        elif s == "U":
            if r - 1 >= 0 and G[r - 1][c] != "#":
                r = r - 1
        elif s == "D":
            if r + 1  < H and G[r + 1][c] != "#":
                r = r + 1
        result.append((r + 1, c + 1))
    return result

H, W, K, T = map(int, input().split())
G = [input() for _ in range(H)]
result = []
for k in range(K):
    r, c, l, s = input().split()
    r, c = int(r) - 1, int(c) - 1
    res = calcData(H, W, G, r, c, s)
    result.append(res[min(len(res) - 1, T - 1)])
print(*result, sep="\n")
