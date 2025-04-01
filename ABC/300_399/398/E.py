from collections import defaultdict

NODE_LIST = set()

def calcList(graph, start_node: int, now_node: int, memo: set, depth: int):
    next_node = graph[now_node]
    if depth >= 3 and depth % 2 == 1:
        if start_node < now_node:
            NODE_LIST.add((start_node, now_node))
    for nn in next_node:
        if nn in memo:
            continue
        memo.add(nn)
        calcList(graph, start_node, nn, memo, depth + 1)
        memo.remove(nn)

def calc():
    return 0, 0

def solve(N, graph):
    myTurn = 0
    turn = 0
    while True:
        if myTurn == turn:
            i, j = calc()
        else:
            i, j = [int(l) for l in input().split()]
            if i == -1 and j == -1:
                break
        turn = 1 - turn

N = int(input())
graph = defaultdict(list)
for n in range(N-1):
    u, v = [int(l) for l in input().split()]
    graph[u].append(v)
    graph[v].append(u)
for i in range(N):
    calcList(graph, i + 1, i + 1, {i + 1}, 0)
print(NODE_LIST)
