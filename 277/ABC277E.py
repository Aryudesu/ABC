# 呼び出し
N, M, K = [int(l) for l in input().split()]
Node = [[-100, -100] for _ in range(N + 1)]
Node[1][1] = 0
branch0 = dict()
branch1 = dict()
for m in range(M):
    u, v, a = [int(l) for l in input().split()]
    if a:
        tmp = branch1.setdefault(u, [])
        tmp.append(v)
        branch1[u] = tmp
        tmp = branch1.setdefault(v, [])
        tmp.append(u)
        branch1[v] = tmp
    else:
        tmp = branch0.setdefault(u, [])
        tmp.append(v)
        branch0[u] = tmp
        tmp = branch0.setdefault(v, [])
        tmp.append(u)
        branch0[v] = tmp
s = set()
if K > 0:
    s = {int(l) for l in input().split()}
now_node = set()
now_node.add(1*(N + 1) + 1)
while now_node and Node[-1][0] < 0 and Node[-1][1] < 0:
    new_node = set()
    for node in now_node:
        a = node // (N + 1)
        n = node % (N + 1)
        now_l = Node[n][a]
        branch = branch1.get(n, []) if a else branch0.get(n, [])
        for b in branch:
            if Node[b][a] < 0 or Node[b][a] > now_l + 1:
                Node[b][a] = now_l + 1
                new_node.add(a * (N + 1) + b)
            if b in s:
                c = 0 if a else 1
                if Node[b][c] < 0 or Node[b][c] > now_l + 1:
                    Node[b][c] = now_l + 1
                    new_node.add(c * (N + 1) + b)
    now_node = new_node
result = Node[-1]
if result[0] >= 0 or result[1] >= 0:
    r0 = result[0]
    r1 = result[1]
    if r0 >= 0 and r1 >= 0:
        print(min(result))
    elif r0 < 0:
        print(r1)
    else:
        print(r0)
else:
    print(-1)
