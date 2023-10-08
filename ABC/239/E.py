import heapq
import sys
sys.setrecursionlimit(10**6)

N, Q = [int(l) for l in input().split()]
X = [int(l) for l in input().split()]


graph = dict()
for n in range(N - 1):
    A, B = [int(l) for l in input().split()]
    tmp = graph.get(A, [])
    tmp.append(B)
    graph[A] = tmp
    tmp = graph.get(B, [])
    tmp.append(A)
    graph[B] = tmp

VK = dict()
VK_Memo = []
for q in range(Q):
    V, K = [int(l) for l in input().split()]
    tmp = VK.get(V, [])
    tmp.append(K)
    VK[V] = tmp
    VK_Memo.append((V, K))
result = dict()


node_memo = [False] * (N + 1)


def get_res(data, node, idx):
    print("===")
    print(data)
    merge_sort(data, idx)
    for k in VK[node]:
        print(data, idx, k)
        res = data[-k]
        result[(node, k)] = res
    print("===")


def calc(data, node):
    data.append(X[node-1])
    node_memo[node] = True
    next_node = graph.get(node, [])
    for nn in next_node:
        if node_memo[nn]:
            continue
        if nn in VK:
            n_idx = len(data) - 1
            print(data, n_idx)
            calc(data, nn)
            get_res(data, nn, n_idx)
        else:
            calc(data, nn)


dat = []
calc(dat, 1)
if 1 in VK:
    get_res(dat, 1, 0)
print(dat)
for vm in VK_Memo:
    print(result[vm])
