N, K = map(int, input().split())
T = list(map(int, input().split()))
T.sort()
result = 0
data = []
for t in T:
    if len(data) >= 1 and t - data[0] > K:
        data = [t]
        result += 1
    else:
        data.append(t)
if data:
    result += 1
print(result)
