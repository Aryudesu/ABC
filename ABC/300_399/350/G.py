N, Q = [int(l) for l in input().split()]
X = 0
graph = dict()
for q in range(Q):
    a, b, c = [int(l) for l in input().split()]
    n = 1 + ((a * (1 + X)) % 998244353) % 2
    u = 1 + ((b * (1 + X)) % 998244353) % N
    v = 1 + ((c * (1 + X)) % 998244353) % N
    if n == 1:
        tmp = graph.get(u, set())
        tmp.add(v)
        graph[u] = tmp
        tmp = graph.get(v, set())
        tmp.add(u)
        graph[v] = tmp
    elif n == 2:
        pass
    else:
        raise Exception()
    print(n, u, v)
