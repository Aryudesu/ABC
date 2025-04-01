from sys import stdin, stdout

# 入力の読み込み
N = int(stdin.readline().strip())
S = stdin.readline().strip()
T = stdin.readline().strip()

# 変換マッピングを記録（辞書）
trans_map = {}
for s, t in zip(S, T):
    if s in trans_map and trans_map[s] != t:
        stdout.write("-1\n")  # 矛盾する変換があれば不可能
        exit()
    trans_map[s] = t

# 変換グラフを作成
from collections import defaultdict

graph = defaultdict(set)
all_chars = set(chr(i) for i in range(ord('a'), ord('z') + 1))
used_chars = set()

for s, t in trans_map.items():
    if s != t:  # 自己変換を除外
        graph[s].add(t)
        used_chars.add(s)
        used_chars.add(t)

# 強連結成分分解（SCC）
from collections import deque


def find_scc(graph):
    index = {}  # 訪問順序
    lowlink = {}  # 最小到達可能順序
    stack = []
    on_stack = set()
    sccs = []
    idx = 0
    
    def dfs(v):
        nonlocal idx
        index[v] = lowlink[v] = idx
        idx += 1
        stack.append(v)
        on_stack.add(v)
        
        for w in graph[v]:
            if w not in index:
                dfs(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif w in on_stack:
                lowlink[v] = min(lowlink[v], index[w])
        
        if index[v] == lowlink[v]:
            scc = []
            while stack:
                node = stack.pop()
                on_stack.remove(node)
                scc.append(node)
                if node == v:
                    break
            if len(scc) > 1:
                sccs.append(scc)
    
    for v in used_chars:
        if v not in index:
            dfs(v)
    
    return sccs

sccs = find_scc(graph)
min_operations = sum(len(scc) - 1 for scc in sccs)
stdout.write(f"{min_operations}\n")
