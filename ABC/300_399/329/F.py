N, Q = [int(l) for l in input().split()]
data = [{int(l)} for l in input().split()]
for q in range(Q):
    a, b = [int(l) for l in input().split()]
    if len(data[b - 1]) < len(data[a - 1]):
        data[a - 1], data[b - 1] = data[b - 1], data[a - 1]
    data[b - 1].update(data[a - 1])
    data[a - 1] = set()
    print(len(data[b - 1]))
