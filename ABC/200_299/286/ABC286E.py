from collections import defaultdict
INF = 10**5

def calc(N, A, graph, u, v, dataset):
    if u in dataset:
        return dataset[u][v]
    nodes = {u}
    max_cost = [(INF, -1)] * N
    max_cost[u] = (0, A[u])
    while nodes:
        new_node = set()
        for node in nodes:
            now_count, now_cost = max_cost[node]
            nexts = graph[node]
            for next_node in nexts:
                next_count, next_cost = max_cost[next_node]
                if now_count + 1 > next_count:
                    continue
                if next_cost >= now_cost + A[next_node]:
                    continue
                new_node.add(next_node)
                max_cost[next_node] = (now_count + 1, now_cost + A[next_node])
        nodes = new_node
    dataset[u] = max_cost
    return dataset[u][v]

N = int(input())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]
dataset = dict()
graph = defaultdict(list)
for i in range(N):
    for j in range(N):
        if S[i][j] == "Y":
            graph[i].append(j)
Q = int(input())
for q in range(Q):
    u, v = map(int, input().split())
    co, res = calc(N, A, graph, u-1, v-1, dataset)
    if res == -1:
        print("Impossible")
    else:
        print(co, res)
