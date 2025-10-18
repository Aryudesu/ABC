from collections import defaultdict

def calc(graph: dict, k: int, node: int, depth: int, memo: dict, S: str, turn: int) -> int:
    if memo[(node, depth, turn)] != 0:
        return memo[(node, depth, turn)]
    # Aが勝ちなら1を返却してAが負けなら-1を返却
    if k * 2 == depth:
        tmp = 1 if S[node] == "A" else -1
        memo[(node, depth, turn)] = tmp
        return tmp
    nextNodes = graph[node]
    for nextNode in nextNodes:
        res = calc(graph, k, nextNode, depth + 1, memo, S, -turn)
        if res == turn:
            memo[(node, depth, turn)] = turn
            return turn
    memo[(node, depth, turn)] = -turn
    return -turn

T = int(input())
result = []
for t in range(T):
    N, M, K = [int(l) for l in input().split()]
    S = input()
    graph = defaultdict(set)
    for m in range(M):
        u, v = [int(l) - 1 for l in input().split()]
        graph[u].add(v)
    memo = defaultdict(int)
    res = calc(graph, K, 0, 0, memo, S, 1)
    result.append(res)
for r in result:
    print("Alice" if r == 1 else "Bob")
