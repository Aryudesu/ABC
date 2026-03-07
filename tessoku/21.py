from collections import defaultdict

N = int(input())
PA = []
for n in range(N):
    p, a = map(int, input().split())
    PA.append((p-1, a))
nodes = defaultdict(int)
nodes[(0, N-1)] = 0
result = 0
while nodes:
    nextNodes = defaultdict(int)
    for l, r in nodes:
        if r < l:
            continue
        nowScore = nodes[(l, r)]
        p, a = PA[l]
        newScore = nowScore
        if l+1 <= p <= r:
            newScore += a
        nextNodes[(l+1, r)] = max(nextNodes[(l+1, r)], newScore)
        result = max(result, newScore)

        p, a = PA[r]
        newScore = nowScore
        if l <= p <= r-1:
            newScore += a
        nextNodes[(l, r-1)] = max(nextNodes[(l, r-1)], newScore)
        result = max(result, newScore)
    nodes = nextNodes
print(result)
