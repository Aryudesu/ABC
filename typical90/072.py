from collections import defaultdict


def calc(depth: int, graph: defaultdict, start: tuple, prev: tuple, node: tuple, memo: set):
    if start == node and depth > 0:
        return depth
    next_node = graph[node]
    result = 0
    for n in next_node:
        if n in memo:
            continue
        if n == prev:
            continue
        memo.add(n)
        result = max(result, calc(depth + 1, graph, start, node, n, memo))
        memo.discard(n)
    return result

H, W = [int(l) for l in input().split()]
C = []
for h in range(H):
    C.append(input())

graph = defaultdict(set)

for h in range(H):
    for w in range(W):
        tmp = (h, w)
        if C[h][w] == "#":
            continue
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if i != 0 and j != 0:
                    continue
                if h + i < 0 or h + i >= H or w + j < 0 or w + j >= W:
                    continue
                if C[h+i][w+j] == "#":
                    continue
                graph[tmp].add((h + i, w + j))


result = 0
for h in range(H):
    for w in range(W):
        if C[h][w] == "#":
            continue
        tmp = calc(0, graph, (h, w), None, (h, w), set())
        result = max(result, tmp)
print(result if result != 0 else -1)
