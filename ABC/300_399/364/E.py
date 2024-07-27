N, X, Y = [int(l) for l in input().split()]
AB = []
for n in range(N):
    AB.append([int(l) for l in input().split()])
data = dict()
data[tuple([0, 0])] = 0
result = 0
for a, b in AB:
    new_data = dict()
    for dat in data:
        x, y = dat
        new_data[tuple([x, y])] = max([data.get(tuple([x, y]), 0), new_data.get(tuple([x, y]), 0)])
        new_x = x + a
        new_y = y + b
        if new_x <= X and new_y <= Y:
            key = tuple([new_x, new_y])
            new_data[key] = max([data.get(dat, 0) + 1, new_data.get(key, 0)])
            result = max([new_data[key], result])
    data = new_data
print(min([result + 1, N]))
