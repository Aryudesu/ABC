import pypyjit

pypyjit.set_param('max_unroll_recursion=-1')

def calc(K, depth: int, graph: dict, node: int, memo: set):
    if depth == K:
        return 1
    nodes = graph.get(node, [])
    tmp = 0
    for n in nodes:
        if not n in memo:
            memo.add(n)
            tmp += calc(K, depth + 1, graph, n, memo)
            memo.discard(n)
    return tmp

H, W, K = [int(l) for l in input().split()]
graph = dict()
S = [input() for _ in range(H)]
for y in range(H):
    for x in range(W):
        num = y * W + x
        if S[y][x] == "#":
            continue
        tmp = graph.get(num, [])
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if (dy == 0 and dx == 0) or (dy != 0 and dx != 0):
                    continue
                if y + dy >= 0 and y + dy < H and x + dx >= 0 and x + dx < W:
                    if S[y + dy][x + dx] != "#":
                        tmp.append((y + dy) * W + x + dx)
        graph[num] = tmp

result = 0
for n in graph:
    result += calc(K, 0, graph, n, {n})
print(result)
