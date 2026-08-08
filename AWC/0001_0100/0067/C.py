INF = 10**12
N, D = map(int, input().split())
# data[日] = 最小何円
data = [INF] * (D + 2)
data[0] = 0
for n in range(N):
    c, f = map(int, input().split())
    for l in range(100):
        newF = f << l
        newC = c << l
        for d in range(D + 1, -1, -1):
            newValue = data[d] + newC
            newDay = min(D + 1, d + newF)
            data[newDay] = min(newValue, data[newDay])
        if newF >= D:
            break
print(min(data[-1], data[-2]))
