N, M = [int(l) for l in input().split()]
graph = dict()
result = dict()
memo = [False] * (N + 1)
for m in range(M):
    a, b, x, y = [int(l) for l in input().split()]
    tmp = graph.get(a, [])
    tmp.append([b, x, y])
    graph[a] = tmp
    tmp = graph.get(b, [])
    tmp.append([a, -x, -y])
    graph[b] = tmp
person = set()
undecidable = set()
result[1] = (0, 0)
person.add(1)
while person:
    next_person = set()
    for p in person:
        px, py = result.get(p)
        pinfo = graph.get(p, [])
        for t in pinfo:
            m, x, y = t
            pos = (x + px, y + py)
            if not memo[m]:
                next_person.add(m)
                memo[m] = True
            # 位置が2箇所になる場合
            p_tmp = result.get(m)
            # その人の特定初
            if p_tmp is None:
                result[m] = pos
            # すでに特定できてた場合で異なる場合
            elif p_tmp != pos:
                undecidable.add(m)
    person = next_person
for n in range(N):
    if result.get(n + 1) is None:
        print("undecidable")
    else:
        if n in undecidable:
            print("undecidable")
        else:
            x, y = result.get(n + 1)
            print(x, y)
