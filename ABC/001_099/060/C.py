N, T = map(int, input().split())
timing = list(map(int, input().split()))
data = []
for t in timing:
    if not data:
        data.append((t, t + T))
    else:
        t1, t2 = data[-1]
        if t > t2:
            data.append((t, t + T))
        else:
            data[-1] = (t1, t + T)
result = 0
for idx in range(len(data)):
    t1, t2 = data[idx]
    result += t2 - t1
print(result)
