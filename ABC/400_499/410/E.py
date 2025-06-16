N, H, M = [int(l) for l in input().split()]
AB = []
for n in range(N):
    AB.append([int(l) for l in input().split()])

data = dict()
data[H] = M
count = 0
for a, b in AB:
    new_data = dict()
    for h in data:
        m = data[h]
        if m - b >= 0:
            if new_data.get(h) is None:
                new_data[h] = m - b
            else:
                new_data[h] = max(m - b, new_data.get(h))
        if h - a >= 0:
            if new_data.get(h - a) is None:
                new_data[h - a] = m
            else:
                new_data[h - a] = max(m, new_data[h - a])
    if not new_data:
        break
    data = new_data
    count += 1
print(count)
