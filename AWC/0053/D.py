from sortedcontainers import SortedSet

N, M = map(int, input().split())
data = [[] for _ in range(N + 1)]
colorMap = dict()
for m in range(M):
    l, r, c = map(int, input().split())
    data[l-1].append(m)
    data[r].append(m)
    colorMap[m] = c
result = [0] * (N + 1)
nums = SortedSet()
maxNum = -1
for n in range(N):
    datList = data[n]
    for m in datList:
        if m in nums:
            nums.discard(m)
            if maxNum == m:
                maxNum = nums[-1] if nums else -1
        else:
            if m > maxNum:
                maxNum = m
            nums.add(m)
    if maxNum >= 0:
        result[n] = colorMap.get(maxNum)
result.pop()
print(*result)
