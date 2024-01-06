N = int(input())
data = []
for x in range(N + 1):
    for y in range(N + 1):
        for z in range(N + 1):
            if x + y + z <= N:
                data.append((x, y , z))
data.sort()
for d in data:
    print(d[0], d[1], d[2])
