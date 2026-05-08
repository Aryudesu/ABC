from collections import defaultdict

def calc(A: list[list[int]], data: dict[int, set[int]], S: int, T: int)->int:
    # 始点と終点が同じであれば1
    if S == T:
        return 0
    sTrains = data[S]
    tTrains = data[T]
    # 1回で終わる場合
    for st in sTrains:
        if st in tTrains:
            return 1
    nodes = sTrains.copy()
    memo  = sTrains.copy()
    count = 1
    while nodes:
        count += 1
        newNodes = set()
        for node in nodes:
            for a in A[node]:
                nextNodes = data[a]
                if len(nextNodes) <= 1:
                    continue
                for nextNode in nextNodes:
                    if nextNode in memo:
                        continue
                    if nextNode in tTrains:
                        return count
                    newNodes.add(nextNode)
                    memo.add(nextNode)
                data[a] = {}
        nodes = newNodes
    return -1


N, M, S, T = map(int, input().split())
data = defaultdict(set)
A = []
for m in range(M):
    K, *a = list(map(int, input().split()))
    A.append(a)
    for adata in a:
        data[adata].add(m)
print(calc(A, data, S, T))
