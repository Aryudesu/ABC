N, M = [int(l) for l in input().split()]
mv = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
data = set()
for m in range(M):
    a, b = [int(l) - 1 for l in input().split()]
    for da, db in mv:
        aa, ab = a + da, b + db
        if aa >= N or aa < 0 or ab >= N or ab < 0:
            continue
        tmp = (aa, ab)
        data.add(tmp)
    tmp = (a, b)
    data.add(tmp)
print(N ** 2 - len(data))
