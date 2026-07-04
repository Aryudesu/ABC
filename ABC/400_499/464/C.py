from collections import defaultdict

N, M = map(int, input().split())
colorNum = N
colorData = [0] * N
colorSet = set()
AB = defaultdict(list)
for n in range(N):
    a, d, b = map(int, input().split())
    AB[d-1].append((a-1, b-1))
    colorSet.add(a-1)
    colorData[a-1] += 1
# print(colorData)
# print(colorSet)
result = []
for m in range(M):
    for a, b in AB[m]:
        colorData[a] -= 1
        if colorData[a] == 0:
            colorSet.discard(a)
        colorData[b] += 1
        colorSet.add(b)
    result.append(len(colorSet))
for r in result:
    print(r)
