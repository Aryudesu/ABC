from atcoder.scc import SCCGraph

N, K = [int(l) for l in input().split()]
X = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
scc = SCCGraph(N)
for n in range(N):
    x = X[n] - 1
    scc.add_edge(n, x)
tp_loop = scc.scc()
loop_data = [-1] * N
for loop in tp_loop:
    if len(loop) == 1:
        l = loop[0]
        if X[l] == l:
            loop_data[l] = 1
    else:
        for l in loop:
            loop_data[l] = len(loop)

result = [None] * N

def calc(node, depth, mod = None):
    if depth == K:
        result[node]
    loop_data

print(loop_data)
