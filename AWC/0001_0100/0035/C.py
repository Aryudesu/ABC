from collections import defaultdict

N, M = map(int, input().split())
T = list(map(int, input().split()))
graph = defaultdict(list)
fuka = [0] * N
teiden = set()
teidenSet = set()
for m in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    fuka[v-1] += 1
    if fuka[v-1] > T[v-1]:
        teiden.add(v-1)
        teidenSet.add(v-1)
while teiden:
    newTeiden = set()
    for node in teiden:
        nextNodes = graph[node]
        for nextNode in nextNodes:
            fuka[nextNode] += 1
            if fuka[nextNode] > T[nextNode]:
                if nextNode not in teidenSet:
                    newTeiden.add(nextNode)
                    teidenSet.add(nextNode)
    teiden = newTeiden
result = []
for res in teidenSet:
    result.append(res + 1)
result.sort()
if result:
    print(*result)
else:
    print(-1)
