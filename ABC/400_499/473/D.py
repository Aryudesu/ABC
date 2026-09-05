def makeInitData(N: int, K: int):
    result = []
    num = K
    for n in range(N, 0, -1):
        if num >= n:
            result.append(num//n)
            num = num % n
        else:
            result.append(0)
    result.reverse()
    return tuple(result)
N, K = map(int, input().split())
result = set()
nodes = set()
initTuple = makeInitData(N, K)
result.add(initTuple)
nodes.add(initTuple)
for p in range(N-1, -1, -1):
    P = p + 1
    nextNodes = set()
    for node in nodes:
        nextNodes.add(node)
        nodeList = list(node)
        while nodeList[p]:
            nodeList[p] -= 1
            for q in range(p-1, -1, -1):
                Q = q + 1
                R = P - Q
                r = R - 1
                if r > q:
                    break
                nodeList[q] += 1
                nodeList[r] += 1
                key = tuple(nodeList)
                nextNodes.add(key)
                result.add(key)
        for s in range(p):
            nodeList = list(node)
            S = s + 1
            while nodeList[p] >= S:
                nodeList[p] -= S
                nodeList[s] += P
                key = tuple(nodeList)
                nextNodes.add(key)
                result.add(key)
    nodes = nextNodes
result = sorted(result)
for res in result:
    print(*res)
