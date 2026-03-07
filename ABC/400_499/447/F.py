from collections import defaultdict

def dfs(graph: dict[int, list[int]], disp: int, node: int, memo: set[int])->int:
    max1, max2 = 0, 0
    for nextNode in graph[node]:
        res = 0
        if len(graph[nextNode]) >= 4:
            if nextNode in memo:
                continue
            memo.add(nextNode)
            res = dfs(graph, disp + 1, nextNode, memo)
        elif len(graph[nextNode]) == 3:
            res = disp + 1
        else:
            continue
        if res > max1:
            max2, max1 = max1, res
        elif res > max2:
            max2 = res
        if disp == 0:
            print("debug2", node, nextNode, max1, max2)
    if len(graph[node]) == 3 and max1 == 0:
        return disp + 1
    if disp > 0:
        return max1
    print("debug", node, max1, max2)
    return max1 + max2 + 1


def calc(N: int, graph: dict[int, list[int]])->int:
    memo = set()
    result = -1
    print(graph)
    for n in range(N):
        if n in memo:
            continue
        memo.add(n)
        if len(graph[n]) < 3:
            continue
        res = dfs(graph, 0, n, memo)
        result = max(result, res)
    return result

Q = int(input())
result = []
for _ in range(Q):
    N = int(input())
    graph = defaultdict(list)
    for n in range(N-1):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    result.append(calc(N, graph))
for r in result:
    print(r)
