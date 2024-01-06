import sys

import pypyjit
from atcoder.dsu import DSU

sys.setrecursionlimit(10**6)
pypyjit.set_param('max_unroll_recursion=-1')

N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
dsu = DSU(N + 1)
graph = dict()
UV = []
# 同じ数値で繋がっているノードは同一視してやる
for m in range(M):
    u, v = [int(l) for l in input().split()]
    UV.append((u, v))
    if A[u-1] == A[v-1]:
        dsu.merge(u, v)

# グラフデータの作成
for m in range(M):
    u, v = UV[m]
    if dsu.same(u, v):
        continue
    # 小さい方から大きい方（一応もしくは同値）の枝をつなぐ
    if A[dsu.leader(u) - 1] <= A[dsu.leader(v) - 1]:
        tmp = graph.get(dsu.leader(u), set())
        tmp.add(dsu.leader(v))
        graph[dsu.leader(u)] = tmp
    if A[dsu.leader(v) - 1] <= A[dsu.leader(u) - 1]:
        tmp = graph.get(dsu.leader(v), set())
        tmp.add(dsu.leader(u))
        graph[dsu.leader(v)] = tmp
# 探索で到達した頂点かのメモ
memo = [False for _ in range(N + 1)]
# その頂点からどれほど進んだらNになるのか
node_memo = [-1 for _ in range(N + 1)]
# Nにたどり着けないノードメモ
death_node = [False for _ in range(N + 1)]

def calc(depth, n):
    # 一度頂点への最長経路を計算したならそれを流用する
    if node_memo[dsu.leader(n)] >= 0:
        return depth + node_memo[dsu.leader(n)]
    # 頂点にたどり着いた場合はdepthを返す
    if dsu.same(n, N):
        return depth
    # そのノードに到着したメモ
    memo[dsu.leader(n)] = True
    result = -1
    # 移動先ノード取得
    nodes = graph.get(dsu.leader(n), [])
    for node in nodes:
        # 移動先が未到着で移動要件を満たしており死にノードでない場合のみ通す
        if memo[dsu.leader(node)] or A[n-1] > A[node-1] or death_node[dsu.leader(node)]:
            continue
        # nodeについて移動した場合の最大値取得
        tmp = calc(depth + 1, dsu.leader(node))
        # 最大値更新
        result = max(result, tmp)
    # ノードnからの最大捜索距離．0より大きくて結果から現在距離引いた分の最大値がソレ
    if result > 0 and node_memo[dsu.leader(n)] <= result - depth:
        node_memo[dsu.leader(n)] = result - depth
    # Nにたどり着けないノードは死にノード
    if result < 0:
        death_node[dsu.leader(n)] = True
    # そのノードに到着したメモの解除
    memo[dsu.leader(n)] = False
    return result

result = calc(1, dsu.leader(1))
print(max(0, result))
