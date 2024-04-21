def calc():
    H, W = [int(l) for l in input().split()]
    A = []
    field = [[0 for _ in range(W)] for _ in range(H)]
    start = None
    goal = None
    for h in range(H):
        tmp = list(input())
        for w in range(W):
            if tmp[w] == "S":
                start = (h, w)
                tmp[w] = "."
            elif tmp[w] == "T":
                goal = (h, w)
                tmp[w] = "."
        A.append(tmp)

    N = int(input())
    RCE = dict()
    for n in range(N):
        r, c, e = [int(l) for l in input().split()]
        RCE[tuple([r - 1, c - 1])] = e

    if not start in RCE:
        return False
    nodes = set()
    nodes.add(tuple(start[0], start[1], 0))
    while nodes:
        new_node = set()
        for node in nodes:
            r, c, e = node
            tmp = RCE.get((r, c), 0)
            if tmp is None:
                continue
            e = tmp
        nodes = new_node
    return False

print("Yes" if calc() else "No")
