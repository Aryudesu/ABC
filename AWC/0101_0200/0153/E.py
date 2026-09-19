from heapq import heappush, heappop

INF = 10 ** 18
N, D = map(int, input().split())
H = list(map(int, input().split()))
days = [INF] * N
data = []
for i in range(N):
    if H[i] <= 0:
        # (何日で感染予定か, インデックス)
        heappush(data, (0, i))
day = 0
while data:
    isOk = False
    while data:
        d, i = heappop(data)
        if d < day:
            continue
        if d > day:
            heappush(data, (d, i))
            break
        if days[i] < INF:
            continue
        isOk = True
        days[i] = day
        if i + 1 < N and days[i + 1] >= INF:
            nd = (H[i + 1] + D - 1) // D
            if i + 2 < N and days[i + 2] < INF:
                h = H[i + 1] - (day - days[i + 2]) * D
                nd = (h + 2 * D - 1) // (2 * D)
            heappush(data, (day + max(1, nd), i + 1))
        if i - 1 >= 0 and days[i - 1] >= INF:
            nd = (H[i - 1] + D - 1) // D
            if i - 2 >= 0 and days[i - 2] < INF:
                h = H[i - 1] - (day - days[i - 2]) * D
                nd = (h + 2 * D - 1) // (2 * D)
            heappush(data, (day + max(1, nd), i - 1))
    if not isOk:
        break
    day += 1
# print(days)
print(N - days.count(INF))
