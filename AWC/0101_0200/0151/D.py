from collections import defaultdict

N, M, K, B = map(int, input().split())
DVT = []
for n in range(N):
    D, V, T = map(int, input().split())
    DVT.append((D, V, T))
# days[何日目][何個受けたか][最後のもの] = 報酬最大値
days = [[defaultdict(int) for _ in range(N)] for _ in range(M + 1)]
days[1][0][-1] = 0
result = 0
for day in range(1, M):
    for count in range(N):
        for last, value in days[day][count].items():
            days[day + 1][count][last] = max(days[day][count][last], days[day + 1][count][last])
            for nextNum in range(last + 1, N):
                d, v, t = DVT[nextNum]
                if day + d >= t:
                    continue
                nextValue = value + v
                if count + 1 == K:
                    nextValue += B
                result = max(result, nextValue)
                days[day + d][count + 1][nextNum] = max(days[day + d][count + 1][nextNum], nextValue)
print(days)
