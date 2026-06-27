from sortedcontainers import SortedSet

N, M, S = map(int, input().split())
data = SortedSet()
for n in range(N):
    data.add(n)
nowPos = S-1
for m in range(M):
    D = int(input())
    data.discard(data[nowPos])
    nowPos = (nowPos + D - 1) % len(data)
    # print(data, nowPos)
print(data[nowPos] + 1)
