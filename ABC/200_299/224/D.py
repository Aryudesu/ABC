def all_swap(graph, data, new_data, memo, goal):
    """全通り走査"""
    dat, idx = data
    nodes = graph.get(idx, [])
    # print(dat, idx)
    # 入れ替えられるものは入れ替える
    for node in nodes:
        tmp = list(dat)
        tmp[idx], tmp[node] = tmp[node], tmp[idx]
        tmp2 = tuple(tmp)
        if goal == tmp2:
            return True
        if not tmp2 in memo:
            memo.add(tmp2)
            tmp3 = tuple([tmp2, node])
            new_data.add(tmp3)
    return False


def calc(graph, start_data):
    """計算"""
    start, node = start_data
    goal = tuple([l + 1 for l in range(9)])
    # print(goal)
    if start == goal:
        return 0
    data = set()
    data.add(start_data)
    memo = set()
    memo.add(start)
    count = 0
    while data:
        count += 1
        new_data = set()
        for dat in data:
            res = all_swap(graph, dat, new_data, memo, goal)
            if res:
                return count
        data = new_data
    return -1

M = int(input())
graph = dict()
for m in range(M):
    u, v = [int(l) - 1 for l in input().split()]
    tmp = graph.get(u, list())
    tmp.append(v)
    graph[u] = tmp
    tmp = graph.get(v, list())
    tmp.append(u)
    graph[v] = tmp

P = [int(l) for l in input().split()]
nums = set([l + 1 for l in range(9)])
for idx in range(8):
    nums.discard(P[idx])
P.append(nums.pop())
node = [0] * 9
for idx in range(9):
    if idx == 8:
        nine = P[idx] - 1
    node[P[idx]-1] = idx + 1
# print(node, nine)
print(calc(graph, tuple([tuple(node), nine])))
