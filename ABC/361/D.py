N = int(input())
S = tuple(input() + ".")
T = tuple(input() + ".")
print(S, T)
stmp= (S, N)
ttmp= (T, N)
bfs = set()
memo = set()
bfs.add(stmp)
memo.add(stmp)
# 幅優先探索
while bfs:
    new_bfs = set()
    # 全ノードに対して
    for dat in bfs:
        st, pos = dat
        # 各文字に対して
        for n in range(N + 1):
            if n == pos:
                continue
    bfs = new_bfs
